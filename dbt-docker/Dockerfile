FROM ghcr.io/dbt-labs/dbt-snowflake:1.7.0

WORKDIR /dbt-docker

# Copy project files
COPY dbt_project.yml .
COPY profiles.yml .
COPY models ./models
COPY entrypoint.sh /entrypoint.sh

ENV USER='ETLPROJECT'
ENV PASSWORD='############'
ENV ACCOUNT='############'
ENV WAREHOUSE='COMPUTE_WH'
ENV DATABASE='PORTFOLIO_ANALYSIS'
ENV SCHEMA='ETL_PROJECT'

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


