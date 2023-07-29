from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(100)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_int(4, 3000)
        res.append(n)
        list_n.append(n)

        a = [gen_int(1, n) for _ in range(n)]
        res.append(a)

    assert sum(list_n) <= 3000

    return res
