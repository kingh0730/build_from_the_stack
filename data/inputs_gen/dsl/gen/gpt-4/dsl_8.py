from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_int(1, 20000)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_int(1, 100000)
        k = gen_int(0, n)
        res.append([n, k])
        list_n.append(n)

        s = "".join([choice(["W", "L"]) for _ in range(n)])
        res.append(s)

    assert sum(list_n) <= 200000

    return res
