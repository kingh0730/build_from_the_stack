from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(10000)
    res.append(t)

    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        k = gen_pos_int(10**6)
        d = gen_pos_int(n)
        res.append([n, k, d])

        a = [gen_pos_int(k) for _ in range(n)]
        res.append(a)

    return res