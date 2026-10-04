import json
import os

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, BASE_DIR
from student_app.logger import get_logger
from student_app.models.student import Student
from student_app.services.calculator import calculate_grade, student_status
from student_app.utils.validation import validate_name, validate_marks
from student_app.reports.student_report import display_report

logger = get_logger(__name__)
DATA_FILE = os.path.join(BASE_DIR, "data", "student.json")


def show_config():
    print("Application :", APP_NAME)
    print("Debug mode  :", DEBUG)
    print("Max students:", MAX_STUDENTS)


def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.error("Student file not found")
        return []
    except json.JSONDecodeError:
        logger.error("Student file is not valid JSON")
        return []

    if isinstance(data, dict):
        return [data]
    return data


def build_student(student_id, name, program, semester, marks):
    if not validate_name(name):
        print("Name cannot be empty")
        logger.warning("Invalid name")
        return None

    if not validate_marks(marks):
        print("Marks must be between 0 and 100")
        logger.warning("Invalid marks: %s", marks)
        return None

    student = Student(student_id, name.strip(), program, semester, marks)
    student.grade = calculate_grade(marks)
    student.status = student_status(marks)
    logger.info("%s got grade %s", student.name, student.grade)
    return student


def read_new_student():
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Name cannot be empty")
        logger.warning("Invalid name")
        return None

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        print("Marks must be a number")
        logger.warning("Marks input was not a number")
        return None

    return build_student("2024100", name, "BS Computer Science", 1, marks)


def main():
    logger.info("Application started")
    show_config()

    shown = 0
    for record in load_students():
        if shown >= MAX_STUDENTS:
            logger.warning("Reached maximum students")
            break

        student = build_student(
            record.get("id", ""),
            record.get("name", ""),
            record.get("program", ""),
            record.get("semester", 1),
            record.get("marks", -1),
        )
        if student is None:
            continue

        display_report(student)
        shown += 1

    answer = input("Add a student? (y/n): ").strip().lower()
    if answer == "y" and shown < MAX_STUDENTS:
        student = read_new_student()
        if student is not None:
            display_report(student)
            shown += 1

    print("Total students:", shown)
    logger.info("Application finished")


if __name__ == "__main__":
    main()
