from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(1024)
    res.append(t)

    for _ in range(t):
        n = gen_pos_int(1024)
        res.append(n)

        s = [gen_pos_int(1023) for _ in range(n)]
        res.append(s)

    return res