"""Module providing a function for logging."""
import logging
import pytest
from src.gd_nasa_pipeline.utils.aws_handler import (
    S3Handler,
)
from src.gd_nasa_pipeline.bronze.extract_data import (
    nc_to_dataframe,
    load_data_to_postgres,
    load_metadata,
)
from src.gd_nasa_pipeline.utils.postgres_handler import PostgresHandler

logger = logging.getLogger(__name__)

aws_handler = S3Handler()

FILE_NAME = "v9/daily/2023/12/power_901_daily_20231216_geos5124_utc.nc"


@pytest.mark.skip(reason="already tested")
def test_file_reader():
    content = aws_handler.read_nc_file(file_name=FILE_NAME)
    logger.info(content)
    assert content is not None


@pytest.mark.skip(reason="already tested")
def test_dataframe_conversion():
    content = aws_handler.read_nc_file(file_name=FILE_NAME)
    df_data = nc_to_dataframe(content)
    logger.info(df_data.columns)
    assert isinstance(df_data, dict)


postgres_handler = PostgresHandler()


@pytest.mark.skip(reason="already tested")
def test_db_loader():
    output = load_data_to_postgres(
        database_name="open_data",
        schema_name="bronze_opendata",
        table_name="s3_power_data",
    )
    logger.info("Loading output: %s", output)
    assert output == 0


def test_metadata():
    content = aws_handler.read_nc_file(file_name=FILE_NAME)
    metadata = load_metadata(content)
    logger.info("the metadata are: %s", metadata)
    assert isinstance(metadata, dict)
