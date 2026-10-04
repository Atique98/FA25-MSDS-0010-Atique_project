# Student Information System

Week 01 project for FA25-MSDS-0010. A small command line app that loads student records from a JSON file, validates them, calculates grades and prints a report. Configuration comes from a `.env` file and everything is covered by pytest.

## Project structure

```
student_project/
├── src/
│   └── student_app/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── logger.py
│       ├── models/
│       │   └── student.py
│       ├── services/
│       │   └── calculator.py
│       ├── utils/
│       │   ├── validation.py
│       │   └── user_input.py
│       └── reports/
│           └── student_report.py
├── tests/
│   ├── test_calculator.py
│   └── test_validation.py
├── data/
│   └── student.json
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set your own values:

```
APP_NAME=Student Information System
DEBUG=True
MAX_STUDENTS=100
API_KEY=...
```

`.env` is ignored by git, only `.env.example` is committed.

## Run

```bash
cd src
python -m student_app.main
```

The app prints the loaded configuration, reads `data/student.json`, prints a report for each valid student and then asks if you want to add more students by hand. Invalid names or marks are rejected with a message instead of crashing. Logs go to the console and to `logs/app.log`.

## Tests

```bash
pytest
```

## Grading scale

| Marks   | Grade |
|---------|-------|
| 80-100  | A     |
| 70-79   | B     |
| 60-69   | C     |
| 50-59   | D     |
| below 50 | F    |
