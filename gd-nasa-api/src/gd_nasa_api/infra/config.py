"""Use this file to access environment variables like the database
username, password, etc.
There is a separate function for each env variable to be retrieved
"""
import os
from typing import Dict

from dotenv import load_dotenv


load_dotenv()


def open_data_config() -> Dict:
    """Return a dictionary with SD
    related database config."""
    return {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASS"),
        "port": os.getenv("DB_PORT"),
        "url": os.getenv("DB_HOST"),
        "db_name": os.getenv("DB_NAME"),
        "schema_name": os.getenv("DB_SCHEMA"),
        "table_name": os.getenv("DB_TABLE"),
    }
