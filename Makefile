.DEFAULT_GOAL := help

test : ## Run all unit tests
	python -m unittest tests.bowling_tests

help: ## Display this help message
	@cat $(MAKEFILE_LIST) | grep -e "^[a-zA-Z_\-]*: *.*## *" | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36,%-30s\033[0m %s\n", $$1, $$2}'

.SILENT: build test lint clean help
