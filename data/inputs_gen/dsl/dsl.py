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


def integer(min, max):
    """
    Returns a random integer between min and max
    """
    return random.randint(min, max)
    raise NotImplementedError


def float(min, max):
    """
    Returns a random float between min and max
    """
    return random.uniform(min, max)
    raise NotImplementedError


def enum(*args):
    """
    Returns a random element from the list of args
    """
    return random.choice(args)
    raise NotImplementedError


def concat_str(*args):
    """
    Returns a string concatenation of all args
    """
    return "".join(args)
    raise NotImplementedError
