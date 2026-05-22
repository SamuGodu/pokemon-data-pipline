````markdown
# Pokémon Data Engineering Pipeline

## Project Overview

This project is an end-to-end Data Engineering pipeline built using Python, PostgreSQL, Docker, and the PokeAPI.

The objective is to simulate a real-world ETL workflow by:

- extracting data from a public REST API
- storing raw API responses
- transforming nested JSON data into relational tables
- loading clean data into PostgreSQL
- preventing duplicate loads
- handling failures and logging events
- documenting the full pipeline professionally

This project focuses on engineering fundamentals, maintainability, and operational thinking instead of unnecessary complexity.

---

# Architecture

```text
PokeAPI
   ↓
Extract Layer (Python)
   ↓
Raw JSON Storage
   ↓
Transform Layer
   ↓
PostgreSQL
   ↓
SQL Analytics & Reporting
```

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- SQL
- Git/GitHub
- PokeAPI

Libraries:

- requests
- pandas
- sqlalchemy
- psycopg2-binary
- python-dotenv

---

# Project Structure

```text
pokemon-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│   ├── schema/
│   └── queries/
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── utils/
│   └── config/
│
├── logs/
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

API Used:

PokeAPI

Endpoints:

- pokemon
- pokemon-species
- type
- ability

Website:

https://pokeapi.co/

---

# Main Features

## API Extraction

- API requests using Python
- Pagination handling
- Raw JSON response storage
- Retry handling for failed requests

## Transformation

- JSON normalization
- Data cleaning
- Missing field handling
- Duplicate prevention

## Database Loading

- PostgreSQL relational schema
- Staging/raw tables
- Final analytics tables
- Incremental loading logic

## Reliability

- Logging system
- Error handling
- Graceful failure management

---

# Database Design

Main tables:

## Raw Layer

- raw_api_responses

## Final Layer

- dim_pokemon
- dim_type
- dim_ability
- fact_pokemon_type
- fact_pokemon_ability

---

# Docker Setup

This project uses Docker Compose to run PostgreSQL locally.

## Start PostgreSQL

```bash
docker-compose up -d
```

## Stop Containers

```bash
docker-compose down
```

---

# Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=pokemon_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
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

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

## Run Extraction

```bash
python src/extract/extract_pokemon.py
```

## Run Transformations

```bash
python src/transform/transform_pokemon.py
```

## Run Database Load

```bash
python src/load/load_pokemon.py
```

---

# SQL Analytics

Example reporting queries:

- Pokémon count by type
- Top 10 heaviest Pokémon
- Most common abilities
- Pokémon with multiple types
- Average stats by type

---

# Logging

Logs are stored in:

```text
logs/
```

Examples:

- API request failures
- malformed JSON
- duplicate rows
- database insertion errors

---

# Future Improvements

Potential future enhancements:

- Airflow orchestration
- Automated scheduling
- Unit testing expansion
- Cloud deployment
- CI/CD integration
- Data validation framework

---

# Challenges Encountered

- Handling nested JSON structures
- Designing relational schemas
- Managing duplicate prevention
- Incremental loading logic
- API reliability handling

---

# Learning Objectives

This project demonstrates:

- ETL fundamentals
- API ingestion
- PostgreSQL database design
- Docker basics
- Logging and reliability
- SQL analytics
- Modular Python structure
- Git workflows
- Operational debugging

---

# Status

Project currently in development.
````
