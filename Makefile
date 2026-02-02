.PHONY: install up down run-api run-cli test lint db-up db-down migration migrate logs

install:
	uv sync

up:
	docker compose up -d

down:
	docker compose down

run-api:
	docker compose up api

logs:
	docker compose logs -f

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
	docker compose up -d db

db-down:
	docker compose down

migration:
	uv run alembic revision --autogenerate -m "$(MSG)"

migrate:
	uv run alembic upgrade head
