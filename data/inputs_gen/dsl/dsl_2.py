from dsl import (
    GENERATE_INPUT,
    gen_pos_int,
    record,
    gen_int,
    to_str_then_concat_with_space,
    all_elements_unique,
)


GENERATE_INPUT


def generate_input():
    t = gen_pos_int(100)
    record(t)

    for _ in range(t):
        n = gen_int(3, 100)
        record(n)

        for _ in range(3):
            sequence = [gen_pos_int(100) for _ in range(n)]
            while not all_elements_unique(sequence):
                sequence = [gen_pos_int(100) for _ in range(n)]
            record(to_str_then_concat_with_space(sequence))
