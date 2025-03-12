"""Module providing a function for logging."""
import logging
from src.gd_nasa_pipeline.gold.silver_to_gold import (
    migrate_table_to_gold,
)


logger = logging.getLogger(__name__)


def test_silver_layer():

    output = migrate_table_to_gold(
        database="open_data",
        table_name="aws_meteo",
        schema_source="silver_opendata",
        schema_destination="gold_opendata",
    )
    logger.info("Loading output: %s", output)
    assert isinstance(output, bool)
