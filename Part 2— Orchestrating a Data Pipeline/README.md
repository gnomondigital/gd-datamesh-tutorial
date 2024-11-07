# NASA Data Pipeline with Apache Airflow

This project is an Apache Airflow data pipeline designed to process and analyze NASA data. The project uses Poetry for dependency management and packaging.

For more details, you can read the article on Medium: [Orchestrating a Data Pipeline](https://medium.com/p/c20a615e9b2b).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/nasa-data-pipeline.git
    cd nasa-data-pipeline
    ```

2. Install Poetry:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install dependencies:
    ```sh
    poetry install
    ```

## Usage

1. Activate the virtual environment:
    ```sh
    poetry shell
    ```

2. Start the Airflow web server and scheduler:
    ```sh
    airflow webserver --port 8080
    airflow scheduler
    ```

3. Access the Airflow web interface at `http://localhost:8080` to monitor and manage your DAGs.

## Project Structure

```
nasa-data-pipeline/
├── dags/
│   └── nasa_data_pipeline.py
├── data/
├── tests/
├── pyproject.toml
└── README.md
```

- `dags/`: Contains the Airflow DAGs.
- `data/`: Directory for storing data files.
- `tests/`: Contains test cases.
- `pyproject.toml`: Poetry configuration file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.