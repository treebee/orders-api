# also include the Docker Compose file of the VSCode config to avoid warnings about orphaned services
dc = docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml
user_id:=$(shell id -u)
group_id:=$(shell id -g)

build:
	docker build . -t orders_api --build-arg USER_ID=$(user_id) --build-arg GROUP_ID=$(group_id)

run:
	$(dc) up -d api

compile-requirements:
	$(dc) run --rm api bash -c "\
		python -m pip install pip-tools && \
		pip-compile -U -o requirements/requirements.txt && \
		pip-compile -U requirements/test-requirements.in -o requirements/test-requirements.txt"

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
	$(dc) run --rm api python -m pytest tests

mypy:
	$(dc) run --rm api mypy src tests

# run all checks, formatting, typing and tests
ci: check-black check-isort mypy flake8 test

bootstrap: build
