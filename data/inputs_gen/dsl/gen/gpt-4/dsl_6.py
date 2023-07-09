from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    T = gen_pos_int(10**4)
    res.append(T)

    n_values = []
    for _ in range(T):
        n = gen_pos_int(2 * 10**5)
        res.append(n)
        n_values.append(n)

        m = gen_pos_int(n * 2)  # Max 2 tracks for each spot
        res.append(m)

        for _ in range(m):
            x = gen_pos_int(n-1)  # x should be less than y
            y = gen_int(x+1, n)  # y should be greater than x
            res.append([x, y])

    assert sum(n_values) <= 2 * 10**5

    return res
