"""import modules"""
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_table(
    source_schema: str,
    source_table: str,
    destination_schema: str,
    destination_table: str,
    columns: str,
):
    """Function to create a new table in schema2 based
    on the structure of table1 in schema1"""
    return f"""DROP TABLE IF EXISTS {destination_schema}.{destination_table};
            CREATE TABLE {destination_schema}.{destination_table}
            AS SELECT {columns} FROM {source_schema}.{source_table};"""
