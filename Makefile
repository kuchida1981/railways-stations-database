.PHONY: install run-api run-cli test lint db-up db-down migration migrate

install:
	uv sync

run-api:
	uv run uvicorn src.main_api:app --reload

run-cli:
	uv run python src/main_cli.py

test:
	uv run pytest

test-cov:
	uv run pytest --cov-report=html

lint:
	uv run ruff check .
	uv run black --check .
	uv run mypy .

format:
	uv run ruff check --fix .
	uv run black .

db-up:
	docker-compose up -d db

db-down:
	docker-compose down

migration:
	uv run alembic revision --autogenerate -m "$(MSG)"

migrate:
	uv run alembic upgrade head