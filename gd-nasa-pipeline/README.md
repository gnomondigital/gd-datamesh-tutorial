# gd-nasa-pipeline

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Pipeline Stages](#pipeline-stages)
- [Tables](#tables)
- [Metadata NASA](#metadata-nasa)
- [Medium content](#medium-content)
- [Contributing](#contributing)
- [Connect with Us](#connect-with-us)

## Overview

The `gd-nasa-pipeline` is a data processing pipeline designed to handle and analyze the NASA Power dataset. This dataset contains various meteorological and solar parameters that are crucial for understanding weather patterns and solar energy potential.

## Features

- **Data Ingestion**: Efficiently ingest data from NASA Power dataset.
- **Data Processing**: Clean and process the data to make it ready for analysis.

## Usage

To run the `gd-nasa-pipeline`, you need to have Poetry installed. Follow these steps:

1. **Make sure you are in the right repository**:
    ```sh
    cd gd-nasa-pipeline
    ```

2. **Create a `.env` file** with the following content:
    ```env
    DB_HOST="xxxx"
    DB_NAME="xxx"
    DB_USER="xxxx"
    DB_PASS="xxxx"
    DB_PORT="xxxx"
    ```

3. **Install dependencies**:
    ```sh
    poetry install
    ```

4. **Run the pipeline**:
    ```sh
    poetry run app --view bronze
    ```

    You can replace `bronze` with `silver` or `gold` depending on the stage of the pipeline you want to execute.

    Alternatively, you can use Docker to run the pipeline:
    ```sh
    docker build -t gd-nasa-pipeline .
    docker run --env-file .env gd-nasa-pipeline --view bronze
    ```

## Pipeline Stages

- **Bronze**: Raw data ingestion from the NASA Power dataset.
- **Silver**: Processed and cleaned data.
- **Gold**: Final clean table in the `gold_opendata` schema.

## Tables

- **s3_power_data**: Raw data stored in S3.
- **geo_referential**: Geographical reference data (available in bronze and silver stages).
- **s3_power_data_final**: Final clean table in the `gold_opendata` schema.

Once all the data is loaded, you will have a clean table in the `gold_opendata` schema in your PostgreSQL database.

## Metadata NASA

The columns in the NASA Power dataset represent various meteorological and solar parameters. Here's what each column means:

| Column       | Description                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------|
| TS_RANGE     | This represents the range of surface air temperature. It's calculated as the difference between the maximum and minimum surface air temperature during a day. |
| CDD18_3      | This stands for Cooling Degree Days (CDD) with a base temperature of 18.3°C. CDD is a measure of the degree of cooling experienced by a location. |
| T2MWET       | This represents the average wet bulb temperature at 2 meters above ground level.                  |
| TS_MAX       | This represents the maximum surface air temperature during a day.                                 |
| DISPH        | This represents the atmospheric stability index, which measures the vertical dispersion of turbulent fluxes. |
| WS10M_MAX    | This represents the maximum wind speed at 10 meters above ground level during a day.              |
| WD2M         | This represents the direction of the wind at 2 meters above ground level.                         |
| WS2M         | This represents the wind speed at 2 meters above ground level.                                    |
| T2MDEW       | This represents the dew point temperature at 2 meters above ground level.                         |
| HDD18_3      | This stands for Heating Degree Days (HDD) with a base temperature of 18.3°C. HDD is a measure of the degree of heating experienced by a location. |
| T2M          | This represents the average temperature at 2 meters above ground level during a day.              |
| QV2M         | This represents the specific humidity at 2 meters above ground level.                             |
| T2M_MAX      | This represents the maximum temperature at 2 meters above ground level during a day.              |
| WS10M_RANGE  | This represents the range of wind speed at 10 meters above ground level during a day.             |
| U50M         | This represents the u component of the wind velocity at 50 meters above ground level.             |
| RHOA         | This represents the air density.                                                                  |
| FRSEAICE     | This represents the fraction of sea ice.                                                          |
| V50M         | This represents the v component of the wind velocity at 50 meters above ground level.             |
| T10M_RANGE   | This represents the range of temperature at 10 meters above ground level during a day.            |
| V2M          | This represents the wind speed at 2 meters above ground level.                                    |
| TQV          | This represents the total column integrated water vapor.                                          |
| TS           | This represents the surface air temperature.                                                      |

## Medium content
You can find more explenations about this code in Medium: [Build ETL Pipelines of Data Domain with Medallion Architecture](https://medium.com/@jason.summer/create-a-gmail-agent-with-model-context-protocol-mcp-061059c07777)
## Contributing

Contributions are welcome

## Connect with Us

- [LinkedIn](https://www.linkedin.com/company/gnomon-digital)
- [Medium](https://medium.com/gnomondigital)
- [Official Website](https://www.gnomondigital.com)