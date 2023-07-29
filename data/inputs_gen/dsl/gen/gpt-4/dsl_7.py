from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(2 * 10**5)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        res.append(n)
        list_n.append(n)

        for _ in range(n):
            m = gen_int(0, n - 1)
            p = gen_int(1, 10**9)
            res.append([m, p])

    assert sum(list_n) <= 2 * 10**5

    return res
