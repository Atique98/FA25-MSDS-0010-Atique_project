from student_app.services.calculator import calculate_grade


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_b():
    assert calculate_grade(75) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_d():
    assert calculate_grade(55) == "D"


def test_grade_f():
    assert calculate_grade(40) == "F"


def test_grade_boundaries():
    assert calculate_grade(80) == "A"
    assert calculate_grade(79) == "B"
    assert calculate_grade(70) == "B"
    assert calculate_grade(69) == "C"
    assert calculate_grade(60) == "C"
    assert calculate_grade(59) == "D"
    assert calculate_grade(50) == "D"
    assert calculate_grade(49) == "F"
