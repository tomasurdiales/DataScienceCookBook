"""Provide state-of-the-art artifical intelligence services.

This module allows the user to perform incredibly powerful mathematical calculations (powered by AI 💅).

Examples:
    >>> from src import very_complex_ai_product
    >>> very_complex_ai_product.add(2, 4)
    6
    >>> very_complex_ai_product.multiply(2.0, 4.0)
    8.0
    >>> from src.very_complex_ai_product import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


def add(a: int | float, b: int | float) -> int | float:
    """Compute and return the sum of two numbers.

    Args:
        a (int | float): A number representing the first addend in the addition.
        b (int | float): A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Calculate the difference of two numbers.

    Args:
        a (int | float): A number representing the minuend in the subtraction.
        b (int | float): A number representing the subtrahend in the subtraction.

    Returns:
        A number representing the difference between `a` and `b`.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Compute and return the product of two numbers.

    Args:
        a (int | float): A number representing the multiplicand in the multiplication.
        b (int | float): A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of `a` and `b`.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Compute and return the quotient of two numbers.

    Args:
        a (int | float): A number representing the dividend in the division.
        b (int | float): A number representing the divisor in the division.

    Returns:
        A number representing the quotient of `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == "__main__":
    pass
