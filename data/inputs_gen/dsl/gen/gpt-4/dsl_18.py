from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    T = gen_pos_int(200)
    res = [T]
    for _ in range(T):
        n = gen_int(2, 200)
        if n % 2 != 0:
            n += 1
        res.append(n)

    return res
