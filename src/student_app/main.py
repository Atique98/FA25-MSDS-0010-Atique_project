import json
import os

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, API_KEY
from student_app.logger import get_logger
from student_app.models.student import Student
from student_app.services.calculator import calculate_grade
from student_app.utils.validation import validate_name, validate_marks, validate_student
from student_app.utils.user_input import get_student_name, get_student_marks, ask_yes_no
from student_app.reports.student_report import display_report

logger = get_logger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_FILE = os.path.join(BASE_DIR, "data", "student.json")


def show_config():
    print(f"Application : {APP_NAME}")
    print(f"Debug mode  : {DEBUG}")
    print(f"Max students: {MAX_STUDENTS}")
    print(f"API key set : {API_KEY is not None}")


def load_students():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.error("Data file not found: %s", DATA_FILE)
        return []
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in %s: %s", DATA_FILE, e)
        return []

    if isinstance(data, dict):
        data = [data]

    logger.info("Loaded %d student record(s) from %s", len(data), DATA_FILE)
    return data


def process_student(data):
    errors = validate_student(data)
    if errors:
        for err in errors:
            logger.warning("Skipping student %s: %s", data.get("id", "?"), err)
        return None

    student = Student.from_dict(data)
    student.grade = calculate_grade(student.marks)
    logger.info("Processed %s -> grade %s", student, student.grade)
    return student


def add_student_manually(next_id):
    name = get_student_name()
    if not validate_name(name):
        logger.warning("Invalid name entered: %r", name)
        print("Name must contain only letters and cannot be empty.")
        return None

    try:
        marks = get_student_marks()
    except ValueError:
        logger.warning("Marks were not a number")
        print("Marks must be a whole number.")
        return None

    if not validate_marks(marks):
        logger.warning("Marks out of range: %s", marks)
        print("Marks must be between 0 and 100.")
        return None

    student = Student(next_id, name.strip(), "Not specified", 1, marks)
    student.grade = calculate_grade(student.marks)
    logger.info("Added %s manually with grade %s", student, student.grade)
    return student


def main():
    logger.info("Starting %s", APP_NAME)
    show_config()

    students = []
    for record in load_students():
        student = process_student(record)
        if student is not None:
            students.append(student)
            display_report(student)

    while len(students) < MAX_STUDENTS:
        if not ask_yes_no("Add another student?"):
            break
        student = add_student_manually(f"MAN{len(students) + 1:03d}")
        if student is not None:
            students.append(student)
            display_report(student)

    if len(students) >= MAX_STUDENTS:
        logger.warning("Reached MAX_STUDENTS limit (%d)", MAX_STUDENTS)

    print(f"Total students processed: {len(students)}")
    logger.info("Finished with %d student(s)", len(students))


if __name__ == "__main__":
    main()
