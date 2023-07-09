"""
The implementation of these functions is controllable.
e.g. if you want to change distribution of random numbers
"""


import random


# To be overridden
from dsl import *


def gen_int(min_inclusive: int, max_inclusive: int):
    """
    Returns a random integer between min (inclusive) and max (inclusive)
    """
    return random.randint(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )


def gen_float(min_inclusive: float, max_inclusive: float):
    """
    Returns a random float between min (inclusive) and max (inclusive)
    """
    return random.uniform(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )
