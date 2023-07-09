from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(10**4)
    res.append(t)

    for _ in range(t):
        a1 = gen_int(1, 100)
        b1 = gen_int(1, 100)
        res.append([a1, b1])

        a2 = gen_int(1, 100)
        b2 = gen_int(1, 100)
        res.append([a2, b2])

    return res
