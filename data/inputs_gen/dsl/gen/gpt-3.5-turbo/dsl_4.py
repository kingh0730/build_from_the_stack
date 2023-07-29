from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(1000)
    res = [t]
    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        res.append(n)

        p = random.sample(range(1, n+1), n)
        res.append(p)

    return res