import pytest
from calculator import calculations


def test_add():
    assert calculations.add(4, 2) == 6
    assert calculations.add(4.0, 2.0) == 6.0
    assert calculations.add(-1, 1) == 0
    assert calculations.add(-1.0, -1.0) == -2.0


def test_calculations_divide_mixed_types():
    assert calculations.divide(4, 2.0) == 2.0
    assert calculations.divide(4.0, 2) == 2.0


def test_calculations_divide_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        calculations.divide(4, 0)


def test_calculations_divide_zero_calculations_dividend():
    assert calculations.divide(0, 2) == 0.0
    assert calculations.divide(0, 2.0) == 0.0
