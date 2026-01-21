## ADDED Requirements
### Requirement: Application Skeleton
The system MUST provide a structured project skeleton including CLI and Web API interfaces.

#### Scenario: Verify Project Structure
- **WHEN** the developer checks the project root
- **THEN** it should contain `src`, `tests`, `pyproject.toml`, and `docker-compose.yml`

### Requirement: Dual Interface Access
The system MUST allow executing the same business logic via both CLI and Web API.

#### Scenario: Execute Sample UseCase via CLI
- **WHEN** the user runs the CLI command `python src/main_cli.py info`
- **THEN** it should display the application version and status

#### Scenario: Execute Sample UseCase via API
- **WHEN** the user requests `GET /info`
- **THEN** it should return the application version and status in JSON format

### Requirement: Database Migration
The system MUST manage database schema changes via migration files.

#### Scenario: Run Migrations
- **WHEN** the developer runs `alembic upgrade head`
- **THEN** the database schema should be updated to the latest version
