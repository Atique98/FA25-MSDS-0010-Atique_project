def get_student_name():
    return input("Enter student name: ")


def get_student_marks():
    raw = input("Enter student marks: ")
    return int(raw)


def ask_yes_no(question):
    answer = input(question + " (y/n): ").strip().lower()
    return answer in ("y", "yes")
