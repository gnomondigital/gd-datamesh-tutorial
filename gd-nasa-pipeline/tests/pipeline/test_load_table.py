"""Module providing a function for logging."""
import logging
from src.gd_nasa_pipeline.utils.aws_handler import (
    S3Handler,
)
import pandas as pd

from gd_nasa_pipeline.utils.postgres_handler import PostgresHandler
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)

aws_handler = S3Handler()


postgres_handler = PostgresHandler()


def test_db_loader():
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    logger.info(df)
    output = postgres_handler.write_dataframe(
        dataset=df,
        database_name="open_data",
        schema_name="bronze_opendata",
        table_name="aws_meteo",
    )
    logger.info("Loading output: %s", output)
    assert output == 0
