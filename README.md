# Projekt Awesome
[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![Made with PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/ "Go to PostgresSQL homepage")
[![Made with Docker](https://img.shields.io/badge/Made_with-Docker-blue?logo=docker&logoColor=white)](https://www.docker.com/ "Go to Docker homepage")
[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/ "Go to Microsoft homepage")
[![OS - macOS](https://img.shields.io/badge/OS-macOS-blue?logo=apple&logoColor=white)](https://www.apple.com/macos/ "Go to Apple homepage")

![20241110_184852](https://github.com/user-attachments/assets/39afc0f2-5e71-414f-984d-944b62211d14)

## Overview
### TLDR
>**You there!** Yes you, in the rush to find what you need and get outa here! Let me show you the way.
This document is meant to guide you in the land of Projekt Awesome - an AI-powered expense tracker. Lemme show you around.

1. **[Overview](#overview)** - You are here! Reading a summary of this document! After that is a summary of the project.
2. **[Quickstart](#quickstart)** - If you just wanna try it out right away
3. **[Orientation](#orientation)** - If you're approved to make changes to the codebase but don't know what's going on
4. **[Credits](#credits)** - List of Contributors and fine print if you wanna say hi or... be bored

>....Oh. You're not in a rush? You wanna read the whole thing? Oh! Well carry on then.

### Project description 
The Expense Tracker project aims to develop a user-friendly web app for seamless expense management with data visualizations and potential AI integration. The application will enable users to record and categorize expenses while providing visual insights into spending patterns. Key goals include core expense tracking features, trend analysis through visual data, and basic AI-driven budget recommendations. Focused on single-user use, the project will maintain simplicity, utilizing local data storage and web-based access optimized for desktop. Deliverables include an efficient, professional expense tracker offering actionable financial insights.

## Quickstart
### Setup
1. Install poetry: `curl -sSL https://install.python-poetry.org | python3 -`
1. Install dependencies: `poetry install`

> See [Poetry docs](https://python-poetry.org/docs/#installing-with-the-official-installer) for details if needed

### Run locally
1. Start poetry shell: `poetry shell`
1. Run app: `streamlit run ./src/app.py` and window will pop up

### Run in Docker
1. Install Docker - https://docs.docker.com/engine/install/
1. Run `docker compose up -d`
1. Navigate to [Streamlit app](http://localhost:8501/) in your browser

>To watch the app logs, run `docker logs expense-tracker-api-1 --follow`, or run `docker compose up` without the `-d` to tail all containers.

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

## Orientation
- Prototyping
    - prototype.py - Original Blueprint
- sample_data
    - mid_data.csv - 200 example records
    - small_data.csv - 10 example records
- src
    - app.py - Ignition
    - expense_manager.py - Initializes database and handles all transaction modification
    - layout.py - Defines app layout
    - tabs
        - aitab.py - Placeholder for AI Chat
        - dailytab.py - All behavior related to daily spending visualization 
        - distributiontab.py - All behavior related to spending distribution visualization
        - expensecolumn.py - All behavior related to database interface
        - overalltab.py - All behavior related to overall spending visualization
    - util
        - constants.py - Defines database characteristics 

## Credits
### Meet the team
- UX/UI Specialist: [Kayla](https://github.com/kayyrey)
- Chief Data Officer: [Mary](https://github.com/marygriffus)
- Front-End Developer: [Mark](https://github.com/mtruitt)
- Back-End Developer: [Kirtan](https://github.com/Kirtant21)
- Team Lead: [Justin](https://github.com/JustinCBlain)

### Terms of use
Projekt Awesome is licensed under [The MIT License](https://github.com/JustinCBlain/Expense-Tracker?tab=MIT-1-ov-file#readme).
