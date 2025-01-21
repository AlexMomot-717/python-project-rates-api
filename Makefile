install:
	poetry install

dev:
    poetry run flask --app rates_api.app:app --debug run

PORT ?= 5000
start:
	poetry run gunicorn -w 5 -b 127.0.0.1:$(PORT) rates_api.app:app

pre-commit:
	pre-commit run --all-files

lint:
	poetry run flake8

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=page_analyzer --cov-report xml --cov-report=html tests/

build-services:
	@docker compose build --no-cache

up:
	@docker compose up -d

down:
	@docker compose down

start-services:
	@docker compose start

stop-services:
	@docker compose stop

restart:
	@docker compose up --build
