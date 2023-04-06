# -*- coding: utf-8 -*-
import random


def generate_two_numbers() -> int:
    """Generate two random integers between 0 and 5.

    Returns: tuple[int, int]
        A tuple of two integers.
    """
    first_int: int = random.randint(0, 6)
    second_int: int = random.randint(0, 6)
    return (first_int, second_int)
