from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


te_input() -> list:
    res = []

    t = gen_pos_int(5000)
    res.append(t)

    for _ in range(t):
        n = gen_pos_int(5000)
        res.append(n)

        for _ in range(n):
            m = gen_pos_int(n-1)
            p = gen_pos_int(10**9)
            res.append([m, p])

    return 