# NASA Data Pipeline with Apache Airflow

This project is a data pipeline built with Apache Airflow to automate the processing and analysis of NASA power data. The pipeline ensures data is fetched, transformed, and stored efficiently on a scheduled basis.

Airflow is a workflow orchestration tool that helps manage complex data processes by defining tasks and dependencies using Directed Acyclic Graphs (DAGs). This allows for scheduling, monitoring, and automating data workflows with ease.

We use Poetry to manage dependencies and packaging, making installation and development seamless.

## Table of Contents

- [NASA Data Pipeline with Apache Airflow](#nasa-data-pipeline-with-apache-airflow)
- [Installation](#installation)
- [Usage](#usage)
- [Understanding Apache Airflow](#understanding-apache-airflow)
- [Project Structure](#project-structure)
- [Conclusion](#conclusion)
- [Connect with Us](#connect-with-us)


## Installation

1. Go to the repository:
    ```sh
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

## Understanding Apache Airflow
Apache Airflow is a powerful orchestration tool that allows for:

**Scheduling tasks:** Define when data should be fetched, processed, or stored.

**Managing dependencies:** Tasks run in a defined order, ensuring a logical workflow.

**Monitoring workflows:** The Airflow UI helps visualize DAG execution, detect failures, and retry tasks when needed.

**Extensibility:** Connectors for databases, APIs, and cloud services make integration easy.

In this project, Airflow is used to automate the data pipeline for NASA power data, ensuring regular and reliable data processing.

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

## Conclusion

This project showcases how Apache Airflow can be used to orchestrate data pipelines, ensuring smooth data ingestion, transformation, and analysis. By leveraging Poetry for dependency management and Airflow for workflow automation, the pipeline remains structured, scalable, and maintainable.

For a deeper dive, read our full article on Medium: [Orchestrating Data Pipelines with Airflow](https://medium.com/gnomondigital/part-2-4-orchestrating-a-data-pipeline-with-airflow-c20a615e9b2b)

## Connect with Us

- [LinkedIn](https://www.linkedin.com/company/gnomon-digital)
- [Medium](https://medium.com/gnomondigital)
- [Official Website](https://www.gnomondigital.com)