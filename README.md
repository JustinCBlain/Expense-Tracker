# Expense-Tracker
UMGC Capstone Project

### Setup
1. Install poetry: `curl -sSL https://install.python-poetry.org | python3 -` (See [Poetry docs](https://python-poetry.org/docs/#installing-with-the-official-installer) for details if needed)
1. Install dependencies: `poetry install`

### Run locally
1. Start poetry shell: `poetry shell`
1. Run app: `streamlit run ./src/app.py` and window will pop up

### Run in Docker
1. Install Docker - https://docs.docker.com/engine/install/
1. Run `docker compose up -d`
1. Navigate to [Streamlit app](http://localhost:8501/) in your browser

To watch the app logs, run `docker logs expense-tracker-api-1 --follow`, or run `docker compose up` without the `-d` to tail all containers.

### Testing and coverage
1. To test, run `poetry run pytest`.
1. To see coverage, run the following:
```
coverage run -m pytest
coverage html
```
Finally, open `htmlcov/index.html` in your browser of choice.
1. To run formatting, run `ruff check --fix src test`
1. To run linting, run `pylint src test/*`