"""
Functions that can be used in the DSL to generate inputs
"""


import random


def gen_int(min_inclusive: int, max_inclusive: int) -> int:
    """
    Returns a random integer between min (inclusive) and max (inclusive)
    """
    return random.randint(min_inclusive, max_inclusive)


def gen_float(min_inclusive: float, max_inclusive: float) -> float:
    """
    Returns a random float between min (inclusive) and max (inclusive)
    """
    return random.uniform(min_inclusive, max_inclusive)


def gen_pos_int(max_inclusive: int) -> int:
    """
    Returns a random integer between 1 and max (inclusive)
    """
    return gen_int(1, max_inclusive)


def gen_neg_int(min_inclusive: int) -> int:
    """
    Returns a random integer between min (inclusive) and -1
    """
    return gen_int(min_inclusive, -1)


def choice(args: list) -> object:
    """
    Chooses a random element from args
    """
    return random.choice(args)


def to_str_then_concat(args: list) -> str:
    """
    Returns a string concatenation of all elements in args
    """
    return "".join(map(str, args))


def to_str_then_concat_with_space(args: list) -> str:
    """
    Returns a string concatenation using space as separator of all elements in args
    """
    return " ".join(map(str, args))


def all_elements_unique(args: list) -> bool:
    """
    Returns true if all elements in args are unique
    """
    return len(set(args)) == len(args)
