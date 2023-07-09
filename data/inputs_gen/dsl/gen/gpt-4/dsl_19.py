from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(10000)
    res.append(t)

    list_n = []
    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        k = gen_pos_int(10**6)
        d = gen_int(1, n)
        res.extend([n, k, d])

        list_n.append(n)

        a = [gen_int(1, k) for _ in range(n)]
        res.append(a)

    assert sum(list_n) <= 2 * 10**5

    return res
