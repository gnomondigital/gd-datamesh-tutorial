import logging
from re import sub
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd

from gd_nasa_pipeline.utils.aws_handler import S3Handler
from gd_nasa_pipeline.utils.postgres_handler import PostgresHandler


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

postgres_handler = PostgresHandler()
aws_handler = S3Handler()


def load_data_to_postgres(
        database_name: str,
        schema_name: str,
        table_name: str) -> Optional[Any]:
    files_names = aws_handler.get_daily_files_from_s3(year=2025)
    dataframes = []

    # Read each file and append its DataFrame to the list
    for file_name in files_names:
        cn_file = aws_handler.read_nc_file(file_name=file_name)
        dataset = nc_to_dataframe(cn_file)
        dataset.columns = map(to_snake_case, dataset.columns)
        dataframes.append(dataset)

    # Combine all DataFrames into one
    combined_dataset = pd.concat(dataframes, ignore_index=True)
    logger.info("Load data to postgres ...")
    output = postgres_handler.write_dataframe(
        dataset=combined_dataset,
        database_name=database_name,
        schema_name=schema_name,
        table_name=table_name,
    )
    logger.info("Data loaded successfully.")
    return output


def to_snake_case(name: str) -> str:
    return "_".join(
        sub(
            "([A-Z][a-z]+)",
            r" \1",
            sub("([A-Z]+)", r" \1", name.replace("-", " ")),
        ).split()
    ).lower()


def nc_to_dataframe(nc_file) -> pd.DataFrame:
    """Convert a netCDF4.Dataset object to a pandas DataFrame"""
    data = {}
    max_len = 0  # Track the maximum length of arrays

    for var in nc_file.variables:
        var_data = np.ravel(nc_file.variables[var][:])
        data[var] = var_data

        # Update max_len if the current variable has a longer length
        max_len = max(max_len, len(var_data))

    # Pad arrays with NaNs to make them of the same length
    for var, var_data in data.items():
        if len(var_data) < max_len:
            data[var] = np.pad(
                var_data, (
                    0,
                    max_len - len(var_data)),
                'constant',
                constant_values=np.nan)

    df = pd.DataFrame(data)
    return df


def load_metadata(nc_file) -> Dict:
    keywords_list = [keyword.strip()
                     for keyword in nc_file.getncattr('keywords').split('>')]

    return {
        'title': nc_file.getncattr('title'),
        'institution': nc_file.getncattr('institution'),
        'project': nc_file.getncattr('project'),
        'source': nc_file.getncattr('source'),
        'history': nc_file.getncattr('history'),
        'summary': nc_file.getncattr('summary'),
        'comment': nc_file.getncattr('comment'),
        'acknowledgement': nc_file.getncattr('acknowledgement'),
        'publisher_name': nc_file.getncattr('publisher_name'),
        'publisher_email': nc_file.getncattr('publisher_email'),
        'keywords': keywords_list,
        'derived_link': nc_file.getncattr('derived_link'),
        'date_created': nc_file.getncattr('date_created'),
    }
