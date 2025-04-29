#!/bin/bash
set -e  # Exit on any error

# Run DBT commands
echo "Running DBT models..."
dbt run

echo "Running DBT tests..."
dbt test

echo "Generating DBT documentation..."
dbt docs generate

echo "Serving DBT documentation..."
dbt docs serve --port 8080 --no-browser