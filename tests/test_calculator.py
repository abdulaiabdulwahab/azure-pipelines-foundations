from src.calculator import add, subtract


def test_add():
    # The pipeline should fail if this assertion fails.
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6