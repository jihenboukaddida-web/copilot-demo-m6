import pytest
from calculator import add, subtract, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.parametrize("divisor", [0, 0.0, -0.0])
def test_divide_by_zero(divisor):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, divisor)
