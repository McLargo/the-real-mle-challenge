.PHONY: help install run

default: help

# Variables
POETRY := $(shell which poetry 2> /dev/null)
POETRY_VERSION = "2.1.1"

help: ## Show help
	@echo "\nUsage:\e[1;36m make [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'


install: ## Install required dependencies
	@if [ -z $(POETRY) ]; then \
		echo "Poetry could not be found, please install version $(POETRY_VERSION)."; \
	else \
		poetry install; \
	fi

run: ## Run train script with arguments: input=<input filename> output=<output filename>
	@if [ -z $(input) ]; then \
		echo "Input file is required. Please provide it as: input=<input filename>"; \
		exit 1; \
	fi
	@if [ -z $(output) ]; then \
		echo "Output file is required. Please provide it as: output=<output filename>"; \
		exit 1; \
	fi
	@poetry run python -m train --input=$(input) --output=$(output)

test: ## Run tests
	@poetry run pytest
	@echo "All tests passed successfully."
