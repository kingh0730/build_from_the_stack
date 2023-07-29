from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(5000)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_pos_int(5000)
        res.append(n)
        list_n.append(n)

        list_mi = [gen_int(0, n - 1) for _ in range(n)]
        list_pi = [gen_pos_int(10**9) for _ in range(n)]

        res.extend([mi, pi] for mi, pi in zip(list_mi, list_pi))
    assert sum(list_n) <= 5000

    return res
