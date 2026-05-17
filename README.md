# DataJob Market Analyst

## Overview

This project is a beginner-level data engineering and analytics pipeline built to practice working with modern data tools in a realistic environment.

The goal of the project is to collect job market data, process it automatically, store it inside a PostgreSQL database, and visualize the results using Apache Superset.

The project was built mainly as a learning experience focused on:

* building ETL pipelines
* working with Airflow DAGs
* containerized development using Docker
* database integration with PostgreSQL
* basic data visualization and analytics
* troubleshooting infrastructure and dependency issues

---

## Project Architecture

```text
Job API / Scraper
        ↓
Python ETL Script
        ↓
Apache Airflow DAG
        ↓
PostgreSQL Database
        ↓
Apache Superset Dashboards
```

---

## Tech Stack

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python                  | Data extraction and processing |
| Apache Airflow          | Workflow orchestration         |
| PostgreSQL              | Data storage                   |
| Apache Superset         | Data visualization             |
| Docker & Docker Compose | Containerized environment      |
| Pandas                  | Data transformation            |

---

## Features

* Automated ETL pipeline using Apache Airflow
* PostgreSQL integration for structured data storage
* Dockerized multi-service environment
* Interactive visualizations in Superset
* Daily scheduled workflow execution
* Basic job market analytics

---

## Database Structure

### Table: `jobs`

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| title    | TEXT    |
| company  | TEXT    |
| location | TEXT    |
| url      | TEXT    |

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <repository-url>
cd DataJob_Market_Analyst
```

### 2. Start containers

```bash
docker-compose up --build
```

### 3. Access services

| Service  | URL                                            |
| -------- | ---------------------------------------------- |
| Airflow  | [http://localhost:8080](http://localhost:8080) |
| Superset | [http://localhost:8088](http://localhost:8088) |

---

## Airflow

The Airflow DAG is responsible for:

1. Running the ETL script
2. Fetching and processing job data
3. Saving results into PostgreSQL

DAG location:

```text
airflow/dags/job_data_pipeline.py
```

---

## Superset

Superset is connected directly to PostgreSQL and used for:

* creating datasets
* exploring SQL queries
* building charts
* creating dashboards

Example visualizations:

* jobs by location
* jobs by company
* most common job titles
* remote vs worldwide offers

---

## Problems Solved During Development

During the project I encountered several infrastructure and configuration issues that helped me better understand the tooling.

Main troubleshooting topics included:

* Docker container management
* Airflow DAG visibility issues
* PostgreSQL connection setup
* Superset database integration
* missing PostgreSQL drivers inside Superset
* Docker rebuild workflow
* container networking
* database schema debugging

---

## What I Learned

This project helped me understand:

* how ETL pipelines work in practice
* how Airflow schedules and executes workflows
* how Docker containers communicate with each other
* how to connect analytics tools to databases
* how to debug environment and dependency problems
* how data flows through a complete analytics stack

---

## Future Improvements

Possible next steps for the project:

* add salary parsing and analysis
* integrate additional job APIs
* improve data cleaning
* create advanced dashboards
* deploy project to cloud environment
* add CI/CD pipeline
* implement dbt transformations
* store historical snapshots for trend analysis

---

# Personal Project Notes

## Initial Goal

The original goal was to create a simple end-to-end data engineering project that simulates a real analytics workflow:

1. collect job data
2. automate the process
3. store the data
4. visualize the results

The project was also meant to help me gain practical experience with tools commonly mentioned in junior data engineering and analytics job offers.

---

# Development Notes

## 1. Project Structure

Created folders:

```text
airflow/
data/
scripts/
sql/
```

Main files:

```text
docker-compose.yml
Dockerfile.superset
README.md
```

---

## 2. Docker Setup

Configured Docker Compose with:

* Airflow webserver
* Airflow scheduler
* PostgreSQL
* Superset

Learned:

* difference between containers and images
* how ports are exposed
* how services communicate internally
* how Docker Compose manages multiple services

Useful commands:

```bash
docker ps

docker-compose up --build

docker-compose down
```

---

## 3. Airflow DAG

Created DAG:

```text
airflow/dags/job_data_pipeline.py
```

Initial issue:

* DAG was not visible in Airflow UI

Troubleshooting:

* checked folder structure
* verified mounted volumes
* restarted containers
* verified Python syntax
* refreshed Airflow UI

Result:

* DAG appeared correctly
* DAG executed successfully

---

## 4. PostgreSQL Integration

Created PostgreSQL container and connected Airflow pipeline.

Verified data insertion manually using SQL queries.

Useful checks:

```sql
SELECT * FROM jobs LIMIT 20;
```

Learned:

* how schemas and tables work
* how PostgreSQL connections are configured
* how to inspect stored data

---

## 5. Superset Problems

This was the biggest troubleshooting section.

Main issue:

Superset could not connect to PostgreSQL.

Error examples:

```text
Could not load database driver
Connection failed
```

Root cause:

* missing PostgreSQL driver inside Superset container

Solution:

Created custom Dockerfile:

```dockerfile
FROM apache/superset

USER root

RUN pip install psycopg2-binary

USER superset
```

Then rebuilt containers:

```bash
docker-compose down

docker-compose up --build
```

Learned:

* how container rebuilds work
* difference between runtime container state and image configuration
* why dependencies inside containers matter

---

## 6. Missing Tools Inside Container

Encountered missing utilities:

* nano was not installed
* pip path issues
* permission issues inside virtual environment

Workarounds used:

* created files using `cat > filename`
* edited files using Neovim from host machine
* rebuilt containers instead of modifying running containers

Important lesson:

Modifying Docker images properly is better than manually patching running containers.

---

## 7. Superset Dataset Creation

Connected Superset to PostgreSQL.

Observed:

* table names differed from expected names
* schema confusion between `public`, `job`, and `jobs`

Final correct table:

```text
public.jobs
```

Created dataset and verified columns:

* id
* title
* company
* location
* url

---

## 8. First Visualization

Created first bar chart in Superset.

Configuration:

* Chart type: Bar Chart
* X-axis: location
* Metric: COUNT(*)

Result:

* successfully visualized number of job offers by location

This confirmed:

* ETL works
* database works
* Superset works
* end-to-end pipeline works

---

# Final Thoughts

This project was my first larger hands-on experience with modern data engineering tooling.

The biggest learning value came from debugging and infrastructure setup rather than writing Python itself.

Working through Docker, Airflow, PostgreSQL, and Superset integration problems helped me understand how real data systems are assembled and maintained.

The project also helped me become more comfortable reading logs, troubleshooting environment issues, and understanding how services communicate inside containerized environments.


