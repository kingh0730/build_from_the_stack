from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(10000)
    res.append(t)

    for _ in range(t):
        n = gen_pos_int(10**5)
        res.append(n)

        a = [choice([-1, 0, 1]) for _ in range(n)]
        res.append(a)

        b = [gen_int(-10**9, 10**9) for _ in range(n)]
        res.append(b)

    return res