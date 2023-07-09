from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    T = gen_pos_int(10**4)
    res.append(T)

    for _ in range(T):
        n = gen_pos_int(10**9)
        g = gen_pos_int(10**9)
        b = gen_pos_int(10**9)

        res.append([n, g, b])

    return res
