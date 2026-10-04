# Student Information System

Week 01 project. The program reads student records from a JSON file, checks the name and marks, calculates a grade, and prints a short report.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

`.env` stays on your machine. It is listed in `.gitignore`.

## Run

```bash
cd src
python -m student_app.main
```

## Test

```bash
pytest
```

Grades: 80 and above A, 70 B, 60 C, 50 D, below 50 F. Status is Pass from 50 upwards, otherwise Fail.
