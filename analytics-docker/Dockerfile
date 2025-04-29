# Use official Python base image
FROM python:3.11-slim

ENV USER='ETLPROJECT'
ENV PASSWORD='#############'
ENV ACCOUNT='###########'
ENV WAREHOUSE='COMPUTE_WH'
ENV DATABASE='PORTFOLIO_ANALYSIS'
ENV SCHEMA='ETL_PROJECT_ANALYTICS'

# Set work directory
WORKDIR /analytics-docker

# Copy files to the container
COPY . /analytics-docker
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]