from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(10000)
    res = [t]
    for _ in range(t):
        n = gen_int(2, 200000)
        res.append(n)

        a = [gen_pos_int(n-1) for _ in range(n)]
        res.append(a)

    return res
