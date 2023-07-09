from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(2 * 10**4)
    res.append(t)

    for _ in range(t):
        n = gen_int(2, 10**5)
        res.append(n)

        p = [i for i in range(1, n+1)]
        random.shuffle(p)
        res.append(p)

    return res