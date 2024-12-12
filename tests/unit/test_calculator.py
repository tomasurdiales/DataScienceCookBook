import pytest

from src import very_complex_ai_product


def test_very_complex_ai_product_add():
    assert very_complex_ai_product.add(4, 2) == 6
    assert very_complex_ai_product.add(4.0, 2.0) == 6.0
    assert very_complex_ai_product.add(-1, 1) == 0
    assert very_complex_ai_product.add(-1.0, -1.0) == -2.0


def test_very_complex_ai_product_divide_mixed_types():
    assert very_complex_ai_product.divide(4, 2.0) == 2.0
    assert very_complex_ai_product.divide(4.0, 2) == 2.0


def test_very_complex_ai_product_divide_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        very_complex_ai_product.divide(4, 0)


def test_very_complex_ai_product_divide_zero_very_complex_ai_product_dividend():
    assert very_complex_ai_product.divide(0, 2) == 0.0
    assert very_complex_ai_product.divide(0, 2.0) == 0.0
