# Welcome to Alvaro's Data Architecture

Hi Data Developer,
This architecture automates the following for you:
- Computer and database configuration (installation, security, user management, etc.)
- [Development](#-development-) and [production](#-production-) guardrails.
- [Pipelines](#-pipelines-) management and orchestration
- [Archival](#-archival-) of unused data
- [Exploration](#-explore-) of the database and data products

All that's left for you to do is:
- [Ingest](#-ingestion-) data into the database with Python scripts
- [Tranform](#-explore-) data in the database with dbt SQL
- [Train](#-development-) AI bots with data from the database

## All you need are computers
### Cloud or your own, up to you, as long as they are connected to the same network.

## Setup
### Are u ready?
- Run the script for your operating system and follow the instructions
    - Windows:
    ``` powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" &&
    uv run configuration\01_local_environment.py
    ```
    - macOS/Linux:
    ``` bash
    curl -LsSf https://astral.sh/uv/install.sh | sh &&
    uv run configuration/01_local_environment.py
    ```

## Ingestion

## dbt

## Explore

## Pipelines

## AI Bots

## Development

## Production

## Unarchive

## Data Health

## Backup