"""Use this file to access environment variables like the database
username, password, etc.
There is a separate function for each env variable to be retrieved
"""
import logging
import os
from typing import Dict

from dotenv import load_dotenv


logger = logging.getLogger(__name__)
load_dotenv()


def open_data_config() -> Dict:
    """Return a dictionary with Open data
    related database config."""
    return {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASS"),
        "port": os.getenv("DB_PORT"),
        "url": os.getenv("DB_HOST"),
        "name": os.getenv("DB_NAME")
    }
