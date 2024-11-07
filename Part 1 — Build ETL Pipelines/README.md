# gd-nasa-pipeline

### Project Structure

This project follows a layered architecture with Bronze, Silver, and Gold layers to manage data processing and transformation.

- **Bronze Layer**: Raw data ingestion and storage.
- **Silver Layer**: Data cleaning, transformation, and enrichment.
- **Gold Layer**: Aggregated and refined data ready for analysis and reporting.

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Poetry for dependency management

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/gd-datamesh-tutorial.git
    cd gd-datamesh-tutorial/Part\ 1\—\Build\ ETL\ Pipelines
    ```

2. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

## metadata nasa:
The columns in the NASA Power dataset represent various meteorological and solar parameters. Here's what each column means:

`TS_RANGE`: This represents the range of surface air temperature. It's calculated as the difference between the maximum and minimum surface air temperature during a day.
`CDD18_3`: This stands for Cooling Degree Days (CDD) with a base temperature of 18.3°C. CDD is a measure of the degree of cooling experienced by a location.
`T2MWET`: This represents the average wet bulb temperature at 2 meters above ground level.
`TS_MAX`: This represents the maximum surface air temperature during a day.
`DISPH`: This represents the atmospheric stability index, which measures the vertical dispersion of turbulent fluxes.
`WS10M_MAX`: This represents the maximum wind speed at 10 meters above ground level during a day.
`WD2M`: This represents the direction of the wind at 2 meters above ground level.
`WS2M`: This represents the wind speed at 2 meters above ground level.
`T2MDEW`: This represents the dew point temperature at 2 meters above ground level.
`HDD18_3`: This stands for Heating Degree Days (HDD) with a base temperature of 18.3°C. HDD is a measure of the degree of heating experienced by a location.
`T2M`: This represents the average temperature at 2 meters above ground level during a day.
`QV2M`: This represents the specific humidity at 2 meters above ground level.
`T2M_MAX`: This represents the maximum temperature at 2 meters above ground level during a day.
`WS10M_RANGE`: This represents the range of wind speed at 10 meters above ground level during a day.
`U50M`: This represents the u component of the wind velocity at 50 meters above ground level.
`RHOA`: This represents the air density.
`FRSEAICE`: This represents the fraction of sea ice.
`V50M`: This represents the v component of the wind velocity at 50 meters above ground level.
`T10M_RANGE`: This represents the range of temperature at 10 meters above ground level during a day.
`V2M`: This represents the wind speed at 2 meters above ground level.
`TQV`: This represents the total column integrated water vapor.
`TS`: This represents the surface air temperature.

### Usage

1. Activate the virtual environment:

    ```sh
    poetry shell
    ```

2. Run the ETL pipeline:

    ```sh
    poetry run app
    ```

### Configuration

Configuration settings for the ETL pipeline can be found in the `config.yaml` file. Update this file with your specific settings.

### Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

### Contributors

This project is created and maintained by Gnomon Digital.

### Acknowledgements

Special thanks to all contributors and the open-source community for their invaluable support and contributions.
