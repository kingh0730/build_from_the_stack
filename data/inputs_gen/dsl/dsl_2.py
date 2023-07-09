from dsl_impl import (
    gen_pos_int,
    gen_int,
    to_str_then_concat_with_space,
    GENERATE_INPUT,
)


GENERATE_INPUT


def generate_input():
    res = []

    t = gen_pos_int(100)
    res.append(t)

    for _ in range(t):
        n = gen_int(3, 100)
        res.append(n)

        with requires_for_each(
            "i",
            lambda a, b, c: a != b and b != c and c != a,
        ):
            a = [gen_pos_int(100) for i in range(n)]
            b = [gen_pos_int(100) for i in range(n)]
            c = [gen_pos_int(100) for i in range(n)]

        a_line = to_str_then_concat_with_space(a)
        b_line = to_str_then_concat_with_space(b)
        c_line = to_str_then_concat_with_space(c)

        res.append(a_line)
        res.append(b_line)
        res.append(c_line)

    return res
