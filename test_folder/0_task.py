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


def add_two_numbers(int_one: int, int_two: int) -> int:
    """Add two integers between 0 and 5.

    Parameters
    ----------
    int_one: int
        An integer between 0 and 5
    int_two: int
        An integer between 0 and 5

    Raises
    ------
    ValueError:
        When either of the integers is less than 0 or greater than 5.
    TypeError:
        When either of the numbers is not an integer

    Returns
    -------
    int:
        The sum of two integers.
    """
    if not isinstance(int_one, int) or not isinstance(int_two, int):
        raise TypeError('The arguments have to be integers.')
    if int_one < 0 or int_one > 5 or int_two < 0 or int_two > 5:
        raise ValueError('Arguments cannot be greater thn 5 or less than 0.')
    return sum(int_one, int_two)
