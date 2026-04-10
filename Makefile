format:
	black tavily-demo.py

install:
	uv pip install tavily-python

publish:
	export UV_PUBLISH_USERNAME="__token__"
	export UV_PUBLISH_PASSWORD="pypi-AgEIcHlwaS5vcmcCJ..."
	uv publish

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Create a virtual environment
	uv venv
	@echo "Virtual environment created. Run 'source $(VENV_NAME)/bin/activate' to use it."

install: ## Install project dependencies
	uv pip install --upgrade pip

lint: ## Check code formatting (requires flake8)
	$(VENV_NAME)/bin/flake8 $(PY_FILES)

test: ## Run unit tests (requires pytest)
	$(VENV_NAME)/bin/pytest tests/

run: ## Run the main application
	uv run main.py

clean: ## Remove temporary files and virtual environment
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete