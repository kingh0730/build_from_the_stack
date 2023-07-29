from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(1000)
    res = [t]
    for _ in range(t):
        a1 = gen_pos_int(10**18)
        k = gen_pos_int(10**16)
        res.extend((a1, k))
    return res