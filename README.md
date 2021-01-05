# Orders API

An example python project serving as a reference. (see also this [blog series](https://www.patrick-muehlbauer.com/articles/python-docker-compose-vscode))

## Development Environment

This projects comes with a `docker-compose` setup and a `Makefile` (yes, a `Makefile` :D) for executing the most frequent commands:

	# building the image
	make setup

	# starting the api service
	make run

	# to access the logs
	make logs

	# executing the tests
	make test

It can also be used with `vscode`.

## pre-commit

To avoid committing and pushing changes that will fail CI because of simple formatting issues, you can install the `pre-commit` hooks.

	# install pre-commit
	pip install --user pre-commit

	# install the hooks
	pre-commit install

Now whenever you commit changes, checks like `black` and `mypy` will be run against the edited files.
