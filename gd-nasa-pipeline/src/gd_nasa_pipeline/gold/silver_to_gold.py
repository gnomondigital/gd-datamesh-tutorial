import logging
from typing import List, Tuple

import pandas as pd

from gd_nasa_pipeline.utils.postgres_handler import PostgresHandler


logger = logging.getLogger(__name__)


def migrate_table_to_gold(
    database: str,
    table_name: str,
    table_name_data: str,
    table_name_ref: str,
    schema_source: str,
    schema_destination: str,
) -> bool:
    postgres_handler = PostgresHandler()

    df1, df2 = get_source_tables(
        database,
        table_name_data,
        table_name_ref,
        schema_source,
        postgres_handler)

    df2 = rename_columns(df2)

    df1, df2 = ensure_column_types_float64(df1, df2, ['lat', 'lon'])

    merged_table = merge_dataframes_on_lat_lon(df1, df2)

    merged_table = add_primary_key(merged_table)

    return write_dataframe_to_postgres(
        merged_table,
        database,
        schema_destination,
        table_name,
        postgres_handler)


def get_source_tables(
    database: str,
    table_name_data: str,
    table_name_ref: str,
    schema_source: str,
    postgres_handler: PostgresHandler
) -> Tuple[pd.DataFrame, pd.DataFrame]:

    logger.info("Getting source tables ...")
    table1 = postgres_handler.get_table(
        db_name=database,
        table_name=table_name_data,
        schema_name=schema_source,
    )
    table2 = postgres_handler.get_table(
        db_name=database,
        table_name=table_name_ref,
        schema_name=schema_source,
    )
    return pd.DataFrame(table1), pd.DataFrame(table2)


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Renaming columns in DataFrame ...")
    return df.rename(columns={'lat': 'lat', 'lng': 'lon'})


def ensure_column_types_float64(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        columns: List[str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    logger.info("Ensuring that specified columns are of type float64 ...")
    for col in columns:
        df1[col] = df1[col].astype(float)
        df2[col] = df2[col].astype(float)
    return df1, df2


def merge_dataframes_on_lat_lon(
        df1: pd.DataFrame,
        df2: pd.DataFrame) -> pd.DataFrame:
    logger.info("Merging the two DataFrames on latitude and longitude...")
    df1['dist'] = abs(df1['lat'].diff().abs() +
                      df1['lon'].diff().abs())
    df2['dist'] = abs(df2['lat'].diff().abs() +
                      df2['lon'].diff().abs())
    # Drop the rows where 'dist' is null
    df1 = df1.dropna(subset=['dist'])
    df2 = df2.dropna(subset=['dist'])
    # Sort the DataFrames by 'dist'
    df1 = df1.sort_values('dist')
    df2 = df2.sort_values('dist')

    merged_table = pd.merge_asof(
        df1, df2, on='dist', direction='nearest')
    return merged_table


def add_primary_key(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Adding primary key ...")
    df['id'] = range(1, len(df) + 1)
    return df


def write_dataframe_to_postgres(
        df: pd.DataFrame,
        database: str,
        schema_destination: str,
        table_name: str,
        postgres_handler: PostgresHandler) -> bool:
    logger.info("Writing DataFrame to Postgres ....")
    return postgres_handler.write_dataframe(
        dataset=df,
        database_name=database,
        schema_name=schema_destination,
        table_name=table_name,
    )
