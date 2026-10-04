from student_app.utils.validation import validate_name, validate_marks, validate_student


def test_valid_marks():
    assert validate_marks(0) is True
    assert validate_marks(50) is True
    assert validate_marks(100) is True


def test_marks_below_zero():
    assert validate_marks(-1) is False
    assert validate_marks(-50) is False


def test_marks_above_hundred():
    assert validate_marks(101) is False
    assert validate_marks(150) is False


def test_marks_wrong_type():
    assert validate_marks("85") is False
    assert validate_marks(None) is False
    assert validate_marks(True) is False


def test_valid_name():
    assert validate_name("Ali") is True
    assert validate_name("Muhammad Atique") is True


def test_invalid_name():
    assert validate_name("") is False
    assert validate_name("   ") is False
    assert validate_name(None) is False
    assert validate_name("Ali123") is False


def test_validate_student_ok():
    data = {"id": "1", "name": "Ali", "program": "BSCS", "semester": 4, "marks": 85}
    assert validate_student(data) == []


def test_validate_student_missing_field():
    data = {"id": "1", "name": "Ali"}
    errors = validate_student(data)
    assert "missing field: marks" in errors
    assert "missing field: program" in errors


def test_validate_student_bad_values():
    data = {"id": "1", "name": "", "program": "BSCS", "semester": 0, "marks": 120}
    errors = validate_student(data)
    assert "invalid name" in errors
    assert "marks must be between 0 and 100" in errors
    assert "semester must be a positive integer" in errors
