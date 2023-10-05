## Postgres

Use the `docker compose` instance of `postgres`.

```
make docker-up
psql -h localhost -U postgres -d postgres
```


## Install

The project uses `pip`, `venv` and `pyproject.toml`. For installing dev dependencies, use

```
python -m venv .venv
source .venv/bin/activate
pip install '.[dev]'
```

## Static Checks

All tools configured using `pyproject.toml`. Use

```
make lint
```

## Alembic

Initial Files created using

```
alembic init alembic_migration
```

Initial setup was done using

```
alembic revision --autogenerate -m "Initial Migration"
```
