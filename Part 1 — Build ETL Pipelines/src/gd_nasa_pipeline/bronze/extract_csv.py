import logging
from typing import Any, Optional

import pandas as pd

from gd_nasa_pipeline.utils.postgres_handler import PostgresHandler


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

postgres_handler = PostgresHandler()


def load_csv_to_postgres(
    database_name: str,
    schema_name: str,
    table_name: str,
    file_path: str = "data/worldcities.csv"
) -> Optional[Any]:
    logger.info("Reading births data from %s", file_path)

    try:
        df_data = pd.read_csv(file_path, sep=",", dtype="str")
        logger.info("Data read successfully.")

        logger.info("Loading data to Postgres...")
        output = postgres_handler.write_dataframe(
            dataset=df_data,
            database_name=database_name,
            schema_name=schema_name,
            table_name=table_name,
        )
        logger.info("Data loaded successfully.")
        return output
    except Exception as e:
        logger.error("Error loading data to Postgres: %s", str(e))
        return None
