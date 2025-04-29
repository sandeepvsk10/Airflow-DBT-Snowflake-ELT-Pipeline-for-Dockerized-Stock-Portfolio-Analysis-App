# Airflow DBT Snowflake ELT Pipeline for Dockerized Stock Portfolio Analysis App

This project implements an ELT pipeline for stock portfolio analysis, leveraging Docker for containerization and Apache Airflow for workflow orchestration. The pipeline is designed to automate the data extraction, transformation, and loading (ETL) processes, followed by data analysis, all within a Dockerized environment. The system interacts with Yahoo Finance API to fetch financial data, processes it using Snowflake and dbt, performs analysis using Python, and visualizes the results with Streamlit.


## Architecture (Data & Infrastructure)
![app-architecture](https://github.com/user-attachments/assets/3aadf2f5-c1b5-46aa-80b0-e35d62f33173)



## Key Problems Trying to Solve
The key problem this project addresses is automating the entire financial data pipeline, from extraction to visualization, in a highly modular and scalable environment. By containerizing each component of the pipeline (Airflow, dbt, Streamlit, ingestion, and analysis scripts), this project creates a reusable, robust system for continuous data processing, analysis, and reporting.


## Demo
Coming soon...



## Technical Overview

This project utilizes several modern technologies to build a scalable and efficient ELT pipeline for financial analysis:

- Airflow: Orchestrates the workflow and automates the pipeline execution.
- dbt (Data Build Tool): Models and transforms raw financial data stored in Snowflake.
- Snowflake: A cloud data warehouse for storing and querying large datasets.
- Yahoo Finance API: Source of stock market and financial data.
- PySpark: Used for large-scale transformations within Snowflake.
- Streamlit: Displays the analysis results in a user-friendly web app.
- Docker: Each component is containerized to ensure isolation, portability, and easy scaling.

  

## Directory Structure

```text
.
├── analytics-docker/
│   ├── dags/
│   └── Dockerfile
├── dbt-docker/
│   ├── models/
│   └── Dockerfile
├── ingestion-docker/
│   ├── scripts/
│   └── Dockerfile
├── orchestration-airflow-docker/
│   ├── scripts/
│   └── Dockerfile
├── LICENSE
└── README.md
```



## Installation
Follow these steps to set up the project locally:


### 1. Install Docker

To run the project components in isolated environments, you must have **Docker** installed.


#### For Windows/Mac:
1. Download Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the instructions.
3. Once installed, open Docker Desktop to start Docker.


#### For Linux:
1. Update the package index:

   ```bash
   sudo apt-get update


### 2. Run the containers using Docker Desktop

You can change the config of each containerized app in Dockerfile and Docker Compose Files



## Results & Explanation

Once set up and running, this pipeline provides a robust financial data processing and analysis framework. 
- The pipeline ensures that the steps of data extraction, transformation, analysis, and visualization are automated and repeatable. Key results include:
- Real-time stock data ingestion from Yahoo Finance.
- Scalable data transformations using dbt and PySpark within Snowflake.
- Efficient orchestration using Airflow to run each task in sequence.
- Interactive visualization in Streamlit for easy consumption of financial insights.



## Growth & Next Steps

1. **Expand Data Sources**: 
   - Integrate more data sources (e.g., other stock market APIs, economic indicators) to enrich the analysis.

2. **Automated Reporting**: 
   - Implement automated reporting features in Streamlit to send daily/weekly stock insights via email or generate downloadable reports.

3. **Scaling**: 
   - Further optimize data processing for larger datasets by integrating more advanced distributed computing techniques.

4. **Performance Monitoring**: 
   - Integrate performance monitoring tools to track the efficiency and reliability of the pipeline.

5. **Cloud Deployment**: 
   - Deploy the entire pipeline to a cloud platform (e.g., AWS, GCP, Azure) for better scalability and fault tolerance.














