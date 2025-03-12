import logging

import click

from gd_nasa_pipeline.bronze.extract_csv import load_csv_to_postgres
from gd_nasa_pipeline.bronze.extract_data import load_data_to_postgres
from gd_nasa_pipeline.gold.silver_to_gold import migrate_table_to_gold
from gd_nasa_pipeline.silver.transform_csv import migrate_geo_table_to_silver
from gd_nasa_pipeline.silver.transform_data import migrate_table_to_silver


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--view", required=True, type=str)
@click.option("--table_name", default="s3_meteo", required=True, type=str)
@click.option("--schema_name", default="bronze_opendata",
              required=True, type=str)
@click.option("--db_name", default="open_data", required=True, type=str)
def run(view: str, table_name: str, schema_name: str, db_name: str) -> None:
    """Run integration of data."""
    click.echo(f"Params --view: {view}")

    if view == "bronze":
        handle_bronze(view, table_name, schema_name, db_name)
    elif view == "silver":
        handle_silver(view, table_name, schema_name, db_name)
    elif view == "gold":
        handle_gold(db_name)
    else:
        raise ValueError(f"View_name {view} is not a validated view name.")


def handle_bronze(view: str,
                  table_name: str,
                  schema_name: str,
                  db_name: str) -> None:
    """Handle Bronze view."""
    if table_name == "s3_meteo":
        load_data_to_postgres(
            database_name=db_name,
            schema_name=schema_name,
            table_name=table_name,
        )
    elif table_name == "geo_referential":
        load_csv_to_postgres(
            database_name=db_name,
            schema_name=schema_name,
            table_name=table_name,
        )
    else:
        logger.info("Incorrect table name.")


def handle_silver(view: str,
                  table_name: str,
                  schema_name: str,
                  db_name: str) -> None:
    """Handle Silver view."""
    if table_name == "s3_meteo":
        migrate_table_to_silver(
            database=db_name,
            table_name=table_name,
            schema_destination="silver_opendata",
            schema_source="bronze_opendata"
        )
    elif table_name == "geo_referential":
        migrate_geo_table_to_silver(
            database=db_name,
            table_name=table_name,
            schema_destination="silver_opendata",
            schema_source="bronze_opendata"
        )
    else:
        logger.info("Incorrect table name.")


def handle_gold(db_name: str) -> None:
    """Handle Gold view."""
    migrate_table_to_gold(
        database=db_name,
        table_name="meteo_with_referential",
        table_name_data="s3_meteo",
        table_name_ref="geo_referential",
        schema_source="silver_opendata",
        schema_destination="gold_opendata",
    )


if __name__ == "__main__":
    run()
