# Pokémon Data Engineering Pipeline

## Overview

This project is an end-to-end ETL pipeline built using Python, PostgreSQL, Docker, and the PokeAPI.

The pipeline extracts Pokémon data from a public REST API, stores raw JSON responses, transforms nested API data into normalized relational tables, and loads the cleaned data into PostgreSQL for analytical querying.

The objective of this project is to demonstrate practical Data Engineering fundamentals including:

- API ingestion
- ETL pipeline design
- relational data modeling
- Dockerized PostgreSQL environments
- incremental loading
- duplicate prevention
- logging and operational debugging
- modular Python project structure

This project intentionally prioritizes engineering fundamentals, maintainability, and reliability over unnecessary complexity.

---

# Architecture

```text
                ┌─────────────┐
                │   PokeAPI   │
                └──────┬──────┘
                       │
                       ▼
             ┌─────────────────┐
             │ Extract Layer   │
             │ Python Requests │
             └────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │ Raw JSON Storage │
            │  data/raw/*.json │
            └────────┬─────────┘
                     │
                     ▼
           ┌────────────────────┐
           │ raw_api_responses  │
           │ PostgreSQL Staging │
           └────────┬───────────┘
                    │
                    ▼
          ┌──────────────────────┐
          │ Transformation Layer │
          │ Normalize JSON Data  │
          └────────┬─────────────┘
                   │
                   ▼
      ┌─────────────────────────────┐
      │ PostgreSQL Analytics Tables │
      │ Dimensions + Fact Tables    │
      └─────────────┬───────────────┘
                    │
                    ▼
           ┌─────────────────┐
           │ SQL Reporting   │
           │ Analytics Layer │
           └─────────────────┘
```

---

# Tech Stack

## Core Technologies

- Python
- PostgreSQL
- Docker
- SQL
- Git/GitHub
- PokeAPI

## Python Libraries

- requests
- psycopg2-binary
- python-dotenv
- pandas
- SQLAlchemy

---

# Project Structure

```text
pokemon-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── schema_diagram.png
│   ├── architecture.png
│   └── reporting.md
│
├── logs/
│   └── pipeline.log
│
├── notebooks/
│   └── json_exploration.ipynb
│
├── sql/
│   ├── schema/
│   │   └── create_tables.sql
│   │
│   └── queries/
│       └── reporting_queries.sql
│
├── src/
│   ├── extract/
│   │   └── extract_pokemon.py
│   │
│   ├── transform/
│   │   └── transform_pokemon.py
│   │
│   ├── load/
│   │   ├── load_raw_response.py
│   │   └── load_clean_tables.py
│   │
│   └── utils/
│       └── logger.py
│
├── tests/
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Data Source

## API

This project uses the public Pokémon REST API:

:contentReference[oaicite:0]{index=0}

## Endpoints Used

- `/pokemon`
- `/type`
- `/ability`
- `/pokemon-species`

---

# Database Design

The project uses a dimensional warehouse-style schema.

## Raw/Staging Layer

### `raw_api_responses`

Stores raw API responses before transformation.

Purpose:

- debugging
- replayability
- raw data preservation
- auditability

---

## Dimension Tables

### `dim_pokemon`

Stores Pokémon-level attributes.

### `dim_type`

Stores Pokémon types.

### `dim_ability`

Stores Pokémon abilities.

---

## Fact Tables

### `fact_pokemon_type`

Many-to-many relationship between Pokémon and types.

### `fact_pokemon_ability`

Many-to-many relationship between Pokémon and abilities.

---

# Features

## API Extraction

- REST API ingestion
- dynamic endpoint requests
- JSON response handling
- local raw JSON storage
- scalable extraction loops

## Data Transformation

- nested JSON normalization
- dimension/fact table generation
- relational modeling
- reusable transformation functions

## Database Loading

- PostgreSQL loading
- conflict handling
- duplicate prevention
- incremental loading logic
- foreign key enforcement

## Reliability & Operations

- pipeline logging
- error handling
- operational debugging
- modular ETL structure

---

# Docker Setup

This project uses Docker Compose to run PostgreSQL locally.

## Start PostgreSQL

```bash
docker-compose up -d
```

## Stop PostgreSQL

```bash
docker-compose down
```

## Verify Running Containers

```bash
docker ps
```

---

# Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=pokemon_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

---

# Installation

## Clone Repository

```bash
git clone <repo_url>
cd pokemon-data-pipeline
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

## 1. Extract Pokémon API Data

```bash
python -m src.extract.extract_pokemon
```

## 2. Load Raw API Responses

```bash
python -m src.load.load_raw_response
```

## 3. Transform and Load Clean Tables

```bash
python -m src.load.load_clean_tables
```

---

# Logging

Pipeline logs are stored in:

```text
logs/pipeline.log
```

The logging system tracks:

- Pokémon loading progress
- pipeline execution
- failures and exceptions
- operational debugging information

Example:

```text
INFO - Loading Pokemon ID 25
INFO - Clean tables loaded successfully
ERROR - Failed processing Pokemon
```

---

# SQL Analytics

Example analytical queries include:

- Pokémon count by type
- Top 10 heaviest Pokémon
- Most common abilities
- Pokémon with multiple types
- Average height by type
- Hidden ability analysis
- Data quality validation checks

---

# Example Pipeline Flow

```text
API Request
    ↓
Raw JSON File
    ↓
raw_api_responses
    ↓
Transformation Layer
    ↓
Dimension Tables
    ↓
Fact Tables
    ↓
Analytics Queries
```

---

# Challenges Encountered

Key engineering challenges addressed during development:

- handling nested API JSON structures
- relational schema normalization
- managing many-to-many relationships
- preventing duplicate inserts
- modularizing ETL logic
- debugging import/package issues
- Docker/PostgreSQL connectivity
- logging and operational observability

---

# Future Improvements

Potential future enhancements:

- orchestration script (`run_pipeline.py`)
- automated scheduling
- Airflow integration
- CI/CD pipeline
- unit testing expansion
- cloud deployment
- data quality validation framework
- retry/backoff API strategy

---

# Learning Outcomes

This project demonstrates practical experience with:

- ETL pipeline development
- REST API ingestion
- PostgreSQL relational modeling
- dimensional warehouse design
- Docker containerization
- modular Python architecture
- logging and observability
- duplicate prevention strategies
- Git/GitHub workflows
- operational debugging

---

# Current Status

Core ETL pipeline functionality is operational and currently supports:

- API extraction
- raw JSON storage
- PostgreSQL staging layer
- transformation layer
- dimensional loading
- fact table loading
- logging
- duplicate prevention
- analytical SQL querying