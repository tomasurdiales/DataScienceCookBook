"""Unit tests for `very_complex_ai_product` module.

The module contains the following functions:

- `test_very_complex_ai_product_add` - Test the very_complex_ai_product.add function.
- `test_very_complex_ai_product_divide_mixed_types` - Test the very_complex_ai_product.divide function with mixed types.
- `test_very_complex_ai_product_divide_zero_divisor` - Test the very_complex_ai_product.divide function with a zero divisor.
- `test_very_complex_ai_product_divide_zero_very_complex_ai_product_dividend` - Test the very_complex_ai_product.divide function with a zero dividend.
"""

import pytest

from src import very_complex_ai_product


def test_very_complex_ai_product_add() -> None:
    """Test very_complex_ai_product.add function with several test cases."""
    assert very_complex_ai_product.add(4, 2) == 6
    assert very_complex_ai_product.add(4.0, 2.0) == 6.0
    assert very_complex_ai_product.add(-1, 1) == 0
    assert very_complex_ai_product.add(-1.0, -1.0) == -2.0


def test_very_complex_ai_product_divide_mixed_types() -> None:
    """Test very_complex_ai_product.divide function with mixed types."""
    assert very_complex_ai_product.divide(4, 2.0) == 2.0
    assert very_complex_ai_product.divide(4.0, 2) == 2.0


def test_very_complex_ai_product_divide_zero_divisor() -> None:
    """Test very_complex_ai_product.divide function with a zero divisor."""
    with pytest.raises(ZeroDivisionError):
        very_complex_ai_product.divide(4, 0)


def test_very_complex_ai_product_divide_zero_very_complex_ai_product_dividend() -> None:
    """Test very_complex_ai_product.divide function with a zero dividend."""
    assert very_complex_ai_product.divide(0, 2) == 0.0
    assert very_complex_ai_product.divide(0, 2.0) == 0.0
