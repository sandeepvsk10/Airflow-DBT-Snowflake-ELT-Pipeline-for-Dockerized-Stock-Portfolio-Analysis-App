FROM python:3.11-slim

ENV USER='ETLPROJECT'
ENV PASSWORD='XXXXXXXXXXXXX'
ENV ACCOUNT='XXXXXXXXXXXXX'
ENV WAREHOUSE='COMPUTE_WH'
ENV DATABASE='PORTFOLIO_ANALYSIS'
ENV SCHEMA='ETL_PROJECT'

WORKDIR /ingestion-docker

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "api_to_snowflake_ingestion.py"]
