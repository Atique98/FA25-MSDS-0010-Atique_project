from student_app.utils.validation import validate_name, validate_marks


def test_valid_marks():
    assert validate_marks(0) is True
    assert validate_marks(50) is True
    assert validate_marks(100) is True


def test_marks_below_zero():
    assert validate_marks(-1) is False


def test_marks_above_hundred():
    assert validate_marks(101) is False


def test_marks_wrong_type():
    assert validate_marks("85") is False
    assert validate_marks(None) is False


def test_valid_name():
    assert validate_name("Ali") is True


def test_invalid_name():
    assert validate_name("") is False
    assert validate_name("   ") is False
    assert validate_name(None) is False
