import logging

from click.testing import CliRunner

from gd_nasa_pipeline.main import run


logger = logging.getLogger(__name__)


def test_run_with_valid_arguments():
    runner = CliRunner()
    result = runner.invoke(run, ["--view", "bronze", "--table_name",
                                 "s3_meteo", "--schema_name",
                                 "bronze_opendata", "--db_name",
                                 "open_data"])

    logger.info(result.output)
    assert result.exit_code == 0
    assert "Params --view : bronze" in result.output


def test_run_with_invalid_arguments():
    runner = CliRunner()
    result = runner.invoke(run, ["--view", "invalid_view", "--table_name",
                           "invalid_table", "--schema_name", "invalid_schema",
                                 "--db_name", "invalid_db"])

    assert result.exit_code != 0
    assert "ValueError" in result.output
