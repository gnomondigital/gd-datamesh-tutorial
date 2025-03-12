"""import modules"""
import logging

from gd_nasa_pipeline.utils.postgres_functions import create_table
from gd_nasa_pipeline.utils.postgres_handler import PostgresHandler


logger = logging.getLogger(__name__)


def migrate_geo_table_to_silver(
    database: str,
    table_name: str,
    schema_source: str,
    schema_destination: str,
) -> bool:
    """Migrate a table to silver_company
    Args:
        conf (Dict): the parsed config file
        pipeline (str): which data to migrate
        function (Any): a process function
    Returns:
        bool: True if succeed
    """
    postgres_handler = PostgresHandler()
    engine = postgres_handler.launch_connection_db(database)

    columns = "city, admin_name, lat, lng, country, capital"
    try:
        with engine.begin() as conn:
            # Create the target table in the target schema
            query = create_table(
                source_schema=schema_source,
                source_table=table_name,
                destination_schema=schema_destination,
                destination_table=table_name,
                columns=columns,
            )
            logger.info("query is : %s", query)
            cursor = conn.connection.cursor()
            cursor.execute(query)
            logger.info("success execution of query: %s", query)

            cursor.close()

    except Exception as e:
        logger.info("Error: %s", str(e))
    finally:
        engine.dispose()
    return True
