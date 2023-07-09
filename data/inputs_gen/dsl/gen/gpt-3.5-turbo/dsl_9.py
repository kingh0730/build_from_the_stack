from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(500)
    res.append(t)

    for _ in range(t):
        s_len = gen_int(1, 100)

        s = "".join([choice(["0", "1"]) for _ in range(s_len)])
        res.append(s)

    return res