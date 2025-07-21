# SkillMate backend project Makefile 
# Usage: make run, make test, make install, etc.

# App entry point (adjusted to actual project structure)
APP=backend.src.main:app

# Virtual environment path
VENV=venv

# Python and pip from virtual environment (Windows style)
PYTHON=$(VENV)/Scripts/python
PIP=$(VENV)/Scripts/pip

# Default target
.DEFAULT_GOAL := help

run: check-venv ## Run FastAPI app with uvicorn
	@$(PYTHON) -m uvicorn $(APP) --reload

test: check-venv ## Run backend tests
	@$(PYTHON) -m pytest -v tests/

install: check-venv ## Install dependencies from requirements.txt
	@$(PIP) install -r requirements.txt

freeze: check-venv ## Save dependencies to requirements.txt
	@$(PIP) freeze > requirements.txt

lint: check-venv ## Lint using Ruff
	@$(PYTHON) -m ruff check .

format: check-venv ## Format code using Ruff
	@$(PYTHON) -m ruff format .

clean: ## Remove __pycache__ folders
	@find . -type d -name "__pycache__" -exec rm -r {} +

db-init: check-venv ## Initialize the database
	@$(PYTHON) -c "from backend.src.data.db import init_db; init_db()"

# check-venv: ## Check if virtual env exists
# 	@if not exist "$(VENV)\Scripts\python.exe" ( \
# 		echo [❌] Virtual environment not found: $(VENV) & \
# 		echo [ℹ️ ] Run: python -m venv $(VENV) && activate it. & \
# 		exit 1 \
# 	) else ( \
# 		echo [✅] Virtual environment found: $(VENV)\Scripts\python.exe \
# 	)

check-venv: ## Check if virtual environment exists and is active
	@setlocal & \
	if not exist "$(PYTHON)" ( \
		echo [❌] Virtual environment not found at $(PYTHON) & \
		echo [ℹ️ ] Run: python -m venv venv && activate it. & \
		exit /b 1 \
	) else ( \
		where python | findstr /I /C:"$(VENV)\Scripts\python.exe" >nul && \
			echo [✅] Virtual environment is ACTIVE: $(PYTHON) || \
			(echo [⚠️ ] Venv exists but NOT activated in shell. Using direct path.) \
	)




help: ## Show available commands
	@echo ""
	@echo "SkillMate Makefile Commands:"
	@echo "-----------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "make %-15s - %s\n", $$1, $$2}'
	@echo ""
