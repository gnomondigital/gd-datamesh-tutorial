"""Module providing a function for logging."""
import logging
from src.gd_nasa_pipeline.silver.transform_data import (
    migrate_table_to_silver,
)


logger = logging.getLogger(__name__)


def test_silver_layer():

    output = migrate_table_to_silver(
        database="open_data",
        table_name="s3_power_data",
        schema_source="bronze_opendata",
        schema_destination="silver_opendata",
    )
    logger.info("Loading output: %s", output)
    assert isinstance(output, bool)
