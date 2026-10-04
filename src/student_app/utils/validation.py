def validate_name(name):
    if name is None:
        return False
    if name.strip() == "":
        return False
    return True


def validate_marks(marks):
    if isinstance(marks, bool) or not isinstance(marks, (int, float)):
        return False
    if marks < 0 or marks > 100:
        return False
    return True
