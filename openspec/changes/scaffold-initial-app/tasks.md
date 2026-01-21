## 1. Environment & Config
- [ ] 1.1 Initialize `uv` project (`pyproject.toml`) with dependencies (fastapi, click, sqlmodel, alembic, asyncpg, pydantic-settings, etc.)
- [ ] 1.2 Create `docker-compose.yml` with PostGIS and Adminer/PgAdmin (optional)
- [ ] 1.3 Setup `src/config.py` using `pydantic-settings` for env vars
- [ ] 1.4 Setup Logging configuration
- [ ] 1.5 Create `Makefile` for common tasks (install, run-api, run-cli, test, lint, db-up)

## 2. Database & Infrastructure
- [ ] 2.1 Setup Alembic (`alembic init -t async`) and configure `env.py` for SQLModel
- [ ] 2.2 Create database connection module (`src/infra/db/engine.py`)
- [ ] 2.3 Create base SQLModel class and a sample model (e.g., `Station`)

## 3. Core (Domain & Use Cases)
- [ ] 3.1 Define Domain Models (if separating from SQLModel, otherwise use SQLModel as hybrid)
- [ ] 3.2 Create a sample Use Case (e.g., `GetVersion`, `CreateStation`) that is independent of HTTP/CLI context

## 4. Interfaces (API & CLI)
- [ ] 4.1 Setup FastAPI app (`src/main_api.py`) and wire up the sample Use Case
- [ ] 4.2 Setup Click app (`src/main_cli.py`) and wire up the sample Use Case
- [ ] 4.3 Verify both interfaces work

## 5. Testing & Quality
- [ ] 5.1 Configure `ruff`, `black`, `mypy` in `pyproject.toml`
- [ ] 5.2 Create `tests/conftest.py` with async DB fixtures
- [ ] 5.3 Write unit test for Use Case
- [ ] 5.4 Write integration test for API
- [ ] 5.5 Write integration test for CLI

## 6. Documentation
- [ ] 6.1 Update README.md with "How to start" instructions
