"""import modules"""
import io
import logging
from contextlib import closing
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import psycopg2
from psycopg2.errors import UndefinedTable
from psycopg2.sql import SQL, Placeholder
from sqlalchemy import create_engine

from gd_nasa_api.infra.config import open_data_config


logger = logging.getLogger(__name__)


class PostgresHandler:
    """class for mapping"""

    def __init__(self, config=open_data_config) -> None:
        config = config()
        self.password = config["password"]
        self.user = config["user"]
        self.port = config["port"]
        self.url = config["url"]
        self.db = config["db_name"]

    def write_dataframe(
        self,
        dataset: pd.DataFrame,
        database_name: str,
        schema_name: str,
        table_name: str,
        if_exists: str = "replace",
    ) -> int:
        """WRITE TABLE IN DB

        Args:
            dataset (pd.DataFrame): the dataset to write
            database_name (str): the db name to write in
            table_name (str): the table to write in the db

        Returns:
            int: length of the dataset
        """
        conn_type = f"postgresql+psycopg2://{self.user}:{self.password}"
        conn_string = f"{conn_type}@{self.url}:{self.port}/{database_name}"
        engine = create_engine(conn_string)

        logger.info("Starting to load into database.")

        dataset.head(0).to_sql(
            table_name,
            engine,
            if_exists=if_exists,
            index=False,
            schema=schema_name,
        )
        logger.debug(dataset.columns)
        conn = engine.raw_connection()
        cur = conn.cursor()
        output = io.StringIO()
        dataset.to_csv(output, sep="\t", header=True, index=False)
        output.seek(0)
        insert_query = (
            f"COPY {schema_name}.{table_name} "
            f"FROM stdin WITH NULL AS '' "
            f"DELIMITER E'\\t' CSV HEADER;"
        )
        cur.copy_expert(insert_query, output)

        conn.commit()
        cur.close()
        conn.close()
        return len(dataset)

    def get_table(
        self,
        db_name: str,
        schema_name: str,
        table_name: str,
        where: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = 0,
        columns: Optional[List] = None,
    ) -> Dict:
        """Read a table rows

        Args:
            db_name (str): the database
            table_name (str): the name of the table
            limit (_type_, optional): an eventual limit. Defaults to None.

        Returns:
            Dict: the dataframe
        """
        try:
            if limit is None:
                limit = f"(SELECT COUNT(*) FROM {schema_name}.{table_name})"

            where = "" if where is None else f"WHERE {where}"
            with closing(
                psycopg2.connect(
                    host=self.url,
                    database=db_name,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                )
            ) as conn:
                with closing(conn.cursor()) as cur:
                    cols = ",".join(columns) if columns else "*"
                    query = (
                        f"SELECT {cols} FROM {schema_name}.{table_name} "
                        f"{where}"
                        f"LIMIT {limit} OFFSET {offset}"
                    )
                    cur.execute(query)
                    column_names = [desc[0] for desc in cur.description]
                    data = []
                    for row in cur.fetchall():
                        row_dict = dict(zip(column_names, row))
                        data.append(row_dict)
                    return data
        except UndefinedTable as ex:
            raise Exception(
                f"The {table_name} does not exist in {db_name}."
            ) from ex

    def execute(
        self,
        query: str,
        db_name: str,
        value: Optional[Tuple[Any]] = None,
        _: Optional[Any] = None,
    ) -> None:
        """Execute a SQL query on the connected PostgreSQL database.

        Parameters
        ----------
        query : str
            The SQL query to execute.
        value : tuple
           The values for the query. Defaults to None.
        _ : Any
            Ignored parameter. Defaults to None.
        Returns
        -------
        None

        """
        with closing(
            psycopg2.connect(
                host=self.url,
                database=db_name,
                user=self.user,
                password=self.password,
                port=self.port,
            )
        ) as conn:
            with closing(conn.cursor()) as cursor:
                if value is not None:
                    logging.debug("Executing the following query: %s .", query)
                    logging.debug("Passing the following value: %s .", value)
                    cursor.execute(query, value)
                else:
                    logging.debug("Executing the following query: %s .", query)
                    cursor.execute(query)
            conn.commit()

    def table_exists(
        self, db_name: str, table_name: str, schema_name: str
    ) -> bool:
        """Check if table exists in the given database or not"""

        exists = False
        try:
            with closing(
                psycopg2.connect(
                    host=self.url,
                    database=db_name,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                )
            ) as conn:
                try:
                    with closing(conn.cursor()) as cur:
                        # Check if the table exists by
                        # attempting to select from it
                        cur.execute(
                            f"SELECT 1 FROM {schema_name}.{table_name} LIMIT 1"
                        )
                        exists = (
                            True  # If the query succeeds, the table exists
                        )
                except psycopg2.Error:
                    pass  # An exception is raised if the table does not exist
                return exists
        except Exception as e:
            logging.error("An error occurred: %s", str(e))

    def check_value_exists(
        self,
        db_name: str,
        table_name: str,
        column_name: str,
        value: str,
        schema_name: str,
    ) -> bool:
        """Check that a value exists in a column"""
        try:
            with closing(
                psycopg2.connect(
                    host=self.url,
                    database=db_name,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                )
            ) as conn:
                with closing(conn.cursor()) as cur:
                    cur.execute(
                        f"SELECT COUNT(*) FROM {schema_name}.{table_name} "
                        f"WHERE {column_name} = '{value}'"
                    )

                    # Fetch the result
                    result = cur.fetchone()

                    # Check if the value exists
                    if result[0] > 0:
                        return True
                    return False
        except Exception as e:
            logging.error("An error occurred: %s", str(e))

    def drop_table(self, db_name: str, table_name: str, schema_name: str):
        """
        Drop a table in a PostgreSQL database.

        Args:
            db_connection (psycopg2.extensions.connection):
            PostgreSQL database connection.
            table_name (str): Name of the table to drop.

        Returns:
            None
        """
        with closing(
            psycopg2.connect(
                host=self.url,
                database=db_name,
                user=self.user,
                password=self.password,
                port=self.port,
            )
        ) as conn:
            try:
                with closing(conn.cursor()) as cur:
                    cur.execute(
                        f"DROP TABLE IF EXISTS {schema_name}.{table_name}"
                    )
                    conn.commit()
                logging.info("Table '%s' has been dropped.", table_name)
            except psycopg2.Error as e:
                conn.rollback()
                logging.error(
                    "An error occurred while dropping the table: %s.", str(e)
                )

    def delete_rows_by_value(
        self,
        db_name: str,
        table_name: str,
        schema_name: str,
        column_name: str,
        values: List,
    ):
        try:
            # Establish a database connection
            with closing(
                psycopg2.connect(
                    host=self.url,
                    database=db_name,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                )
            ) as conn:
                with closing(conn.cursor()) as cur:
                    placeholders = ", ".join(["%s"] * len(values))
                    delete_query = f"""
                        DELETE FROM {schema_name}.{table_name}
                        WHERE {column_name} IN ({placeholders});
                    """

                    cur.execute(delete_query, values)
                    conn.commit()

        except psycopg2.Error as e:
            logging.error("Error deleting rows: %s", e)

    def column_exists(
        self,
        db_name: str,
        table_name: str,
        schema_name: str,
        column_name: str,
    ):
        try:
            # Establish a database connection
            with closing(
                psycopg2.connect(
                    host=self.url,
                    database=db_name,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                )
            ) as conn:
                with closing(conn.cursor()) as cur:
                    query = SQL(
                        """SELECT column_name
                               FROM information_schema.columns
                               WHERE table_schema = {} AND table_name = {}
                               AND column_name = {};
                    """
                    ).format(
                        Placeholder(),
                        Placeholder(),
                        Placeholder(),
                    )
                    cur.execute(query, (schema_name, table_name, column_name))
                    conn.commit()
                    result = cur.fetchone()
                    if result:
                        return True
                    return False
        except psycopg2.Error as e:
            logging.error("Error deleting rows: %s", e)

    def launch_connection_db(self, database_name: str = None):
        """create a connection"""
        if database_name is None:
            database_name = self.db
        conn_type = f"postgresql+psycopg2://{self.user}:{self.password}"
        conn_string = f"{conn_type}@{self.url}:{self.port}/{database_name}"
        engine = create_engine(conn_string)
        return engine
