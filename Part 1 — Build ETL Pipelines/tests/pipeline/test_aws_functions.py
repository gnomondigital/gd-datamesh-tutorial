"""Module providing a function for logging."""
import logging
import pytest
from src.gd_nasa_pipeline.utils.aws_handler import (
    S3Handler,
)


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

aws_handler = S3Handler()

FILE_NAME = "v9/climatology/power_901_climatology_meteorology_utc.nc"


@pytest.mark.skip(reason="already tested")
def test_data_extractor():
    answers = aws_handler.get_daily_files_from_s3()
    logger.info(answers)
    assert isinstance(answers, list)
    assert len(answers) > 0


@pytest.mark.skip(reason="already tested")
def test_climatology_extractor():
    answers = aws_handler.get_climatology_files_from_s3()
    logger.info(answers)
    assert isinstance(answers, list)
    assert len(answers) > 0


def test_file_reader():
    content = aws_handler.read_nc_file(file_name=FILE_NAME)
    logger.info(content.getncattr('title'))
    assert content is not None
