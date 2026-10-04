def generate_report(student):
    lines = [
        "--- Student Report ---",
        f"ID       : {student.id}",
        f"Name     : {student.name}",
        f"Program  : {student.program}",
        f"Semester : {student.semester}",
        f"Marks    : {student.marks}",
        f"Grade    : {student.grade}",
    ]
    return "\n".join(lines)


def display_report(student):
    print()
    print(generate_report(student))
    print()
