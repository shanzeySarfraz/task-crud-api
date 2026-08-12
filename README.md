# Task CRUD API — SQLite

A simple CRUD API built with FastAPI and SQLite.

## Features

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks
- SQLite database persistence
- Automatic database and table creation
- Three example tasks are inserted on the first run
- Data survives server restarts
- Swagger/OpenAPI documentation

## Technology Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## Database

SQLite was chosen because it is lightweight and does not require a separate database server.

The database file is:

```text
tasks.db