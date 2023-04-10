# also include the Docker Compose file of the VSCode config to avoid warnings about orphaned services
dc = docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml
user_id:=$(shell id -u)
group_id:=$(shell id -g)

build:
	docker build . -t orders_api --build-arg USER_ID=$(user_id) --build-arg GROUP_ID=$(group_id)

setup-db:
	$(dc) run --rm api alembic upgrade head

run:
	$(dc) up -d api

delete-db:
	$(dc) stop db
	$(dc) rm -v db
	$(dc) up -d db
	sleep 2

recreate-db: delete-db setup-db

insert-mockdata:
	$(dc) run --rm api python -m orders_api.mock

compile-requirements:
	$(dc) run --rm api bash -c "\
		python -m pip install -U pip-tools && \
		pip-compile -U --resolver=backtracking -o requirements/requirements.txt && \
		pip-compile -U --resolver=backtracking requirements/test-requirements.in -o requirements/test-requirements.txt"

alembic-revision:
	$(dc) run --rm api alembic revision --autogenerate -m $(msg)

logs:
	$(dc) logs -f

check-black:
	$(dc) run --rm api black --check src tests

black:
	$(dc) run --rm api black src tests

check-isort:
	$(dc) run --rm api isort src tests --check

isort:
	$(dc) run --rm api isort src tests

flake8:
	$(dc) run --rm api flake8 src tests

test:
	$(dc) run --rm -e POSTGRES_DB="order_api_testdb" api python -m pytest tests -sv

test-cov:
	$(dc) run --rm -e POSTGRES_DB="order_api_testdb" api python -m pytest tests -sv --cov orders_api --cov-report html

test-cov-term:
	$(dc) run --rm -e POSTGRES_DB="order_api_testdb" api python -m pytest tests -sv --cov orders_api --cov-report term-missing

mypy:
	$(dc) run --rm api mypy src tests

# run all checks, formatting, typing and tests
ci: check-black check-isort mypy flake8 test

bootstrap: build setup-db
