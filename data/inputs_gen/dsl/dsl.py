"""
The implementation of these functions is controllable.
e.g. if you want to change distribution of random numbers
"""
import random


def record(arg: int | float | str):
    """
    Records the argument
    """
    print(arg)


def gen_int(min_inclusive: int, max_inclusive: int):
    """
    Returns a random integer between min and max
    """
    return random.randint(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )


def gen_float(min_inclusive: float, max_inclusive: float):
    """
    Returns a random float between min and max
    """
    return random.uniform(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )


def gen_pos_int(max_inclusive: int):
    """
    Returns a random integer between 1 and max
    """
    return gen_int(1, max_inclusive)


def gen_neg_int(min_inclusive: int):
    """
    Returns a random integer between min and -1
    """
    return gen_int(min_inclusive, -1)


def enum(*args):
    """
    Returns a random element from the list of args
    """
    return random.choice(args)


def concat_str(*args):
    """
    Returns a string concatenation of all args
    """
    return "".join(args)
