from dsl import (
    GENERATE_INPUT,
    gen_pos_int,
    record,
    gen_int,
    to_str_then_concat_with_space,
    requires_for_each,
)


GENERATE_INPUT


def generate_input():
    t = gen_pos_int(100)
    record(t)

    for _ in range(t):
        n = gen_int(3, 100)
        record(n)

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

        record(a_line)
        record(b_line)
        record(c_line)
