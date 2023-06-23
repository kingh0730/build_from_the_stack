"""
The implementation of these functions is controllable.
e.g. if you want to change distribution of random numbers
"""
import random


def record(arg):
    """
    Records the argument
    """
    print(arg)


def integer(min_inclusive, max_inclusive):
    """
    Returns a random integer between min and max
    """
    return random.randint(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )


def float(min_inclusive, max_inclusive):
    """
    Returns a random float between min and max
    """
    return random.uniform(
        min_inclusive,
        min(max_inclusive, min_inclusive + 4),
    )


def positive_integer(max_inclusive):
    """
    Returns a random integer between 1 and max
    """
    return integer(1, max_inclusive)


def negative_integer(min_inclusive):
    """
    Returns a random integer between min and -1
    """
    return integer(min_inclusive, -1)


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
