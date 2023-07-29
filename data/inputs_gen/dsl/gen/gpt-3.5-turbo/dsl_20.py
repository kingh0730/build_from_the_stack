from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    q = gen_pos_int(500)
    res = [q]
    for _ in range(q):
        n = gen_pos_int(100)
        m = gen_int(-10**9, 10**9)
        res.append([n, m])

        for _ in range(n):
            t = gen_pos_int(10**9)
            l = gen_int(-10**9, 10**9)
            h = gen_int(l, 10**9)
            res.append([t, l, h])

    return res