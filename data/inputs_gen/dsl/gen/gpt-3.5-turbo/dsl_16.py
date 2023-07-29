from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    tc = gen_int(1, 20)
    res = [tc]
    for _ in range(tc):
        n = gen_int(1, 100)
        res.append(n)

        C = gen_float(0.001, 9.999)
        T = gen_float(0, 200000)
        res.append([C, T])

        for _ in range(n):
            a = gen_int(1, 10000)
            p = gen_int(1, 10)
            res.append([a, p])

    return res