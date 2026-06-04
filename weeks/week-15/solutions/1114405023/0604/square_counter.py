"""Square counter implementation."""


def count_squares(a: int, b: int) -> int:
    """Return the number of perfect squares in the inclusive range [a, b]."""
    if a > b:
        raise ValueError("a must be <= b")

    count = 0
    number = 0

    while number * number <= b:
        square = number * number

        if a <= square <= b:
            count += 1

        number += 1

    return count