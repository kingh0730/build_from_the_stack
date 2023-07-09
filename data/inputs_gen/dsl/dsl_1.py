from dsl_impl import (
    gen_pos_int,
    to_str_then_concat_with_space,
    GENERATE_INPUT,
)


GENERATE_INPUT


def generate_input() -> list:
    res = []

    q = gen_pos_int(10**4)
    res.append(q)

    for _ in range(q):
        ni = gen_pos_int(10**18)
        mi = gen_pos_int(10**18)
        ki = gen_pos_int(10**18)

        line = to_str_then_concat_with_space([ni, mi, ki])
        res.append(line)

    return res
