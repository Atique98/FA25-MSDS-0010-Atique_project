def validate_name(name):
    if name is None:
        return False
    name = name.strip()
    if name == "":
        return False
    if not all(ch.isalpha() or ch.isspace() for ch in name):
        return False
    return True


def validate_marks(marks):
    if isinstance(marks, bool):
        return False
    if not isinstance(marks, (int, float)):
        return False
    if marks < 0 or marks > 100:
        return False
    return True


def validate_student(data):
    errors = []
    required = ["id", "name", "program", "semester", "marks"]
    for key in required:
        if key not in data:
            errors.append(f"missing field: {key}")
    if errors:
        return errors

    if not validate_name(data["name"]):
        errors.append("invalid name")
    if not validate_marks(data["marks"]):
        errors.append("marks must be between 0 and 100")
    if not isinstance(data["semester"], int) or data["semester"] < 1:
        errors.append("semester must be a positive integer")
    return errors
