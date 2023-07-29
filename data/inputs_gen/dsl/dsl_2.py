from dsl_impl import (
    gen_pos_int,
    gen_int,
    to_str_then_concat_with_space,
    GENERATE_INPUT,
)


GENERATE_INPUT


def generate_input() -> list:
    t = gen_pos_int(100)
    res = [t]
    for _ in range(t):
        n = gen_int(3, 100)
        res.append(n)

        a = [gen_pos_int(100) for _ in range(n)]
        res.append(a)

        b = [gen_pos_int(100) for _ in range(n)]
        res.append(b)

        c = [gen_pos_int(100) for _ in range(n)]
        res.append(c)

        for i in range(n):
            assert a[i] != b[i] and a[i] != c[i] and b[i] != c[i]

    return res
