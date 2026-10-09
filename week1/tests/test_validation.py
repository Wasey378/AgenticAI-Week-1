from src.Utils.Validate import validate_marks, validate_name


def test_valid_name():
    assert validate_name("Ali") is True


def test_empty_name():
    assert validate_name("") is False


def test_valid_marks():
    assert validate_marks(85) is True


def test_minimum_marks_boundary():
    assert validate_marks(0) is True


def test_maximum_marks_boundary():
    assert validate_marks(100) is True


def test_negative_marks():
    assert validate_marks(-10) is False


def test_marks_above_limit():
    assert validate_marks(150) is False


def test_marks_below_minimum_boundary():
    assert validate_marks(-1) is False

0
def test_marks_above_maximum_boundary():
    assert validate_marks(101) is False
