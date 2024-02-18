.DEFAULT_GOAL := help

###############################################################################
# Tests
###############################################################################
.PHONY: test, test-verbose

test: ## Run all unit tests
	@pytest  tests/

test-verbose: ## Run all unit tests (with one level of verbose and outputs)
	@pytest -v -s tests/

###############################################################################
# Dependencies
###############################################################################
.PHONY: dependency-update

dependency-update: ## Update poetry dependencies
	@poetry install

###############################################################################
# Execution
###############################################################################
.PHONY: run

run: ## Execute the code
	@python streaming_converter/__main__.py

###############################################################################
# Utils
###############################################################################
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
