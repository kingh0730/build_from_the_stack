from dsl import (
    gen_pos_int,
    record,
    gen_int,
    to_str_then_concat_with_space,
    INPUT_GENERATOR,
)


INPUT_GENERATOR


def generate_input():
    t = gen_pos_int(1000)
    record(t)

    for _ in range(t):
        n = gen_int(2, 2 * 10**5)
        k = gen_int(1, n - 1)

        nk_line = to_str_then_concat_with_space([n, k])
        record(nk_line)

        barrels = [gen_int(0, 10**9) for _ in range(n)]
        barrels_line = to_str_then_concat_with_space(barrels)
        record(barrels_line)
