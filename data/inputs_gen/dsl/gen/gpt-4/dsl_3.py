from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    res = []

    t = gen_pos_int(1000)
    res.append(t)

    sum_n = 0
    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        sum_n += n
        assert sum_n <= 2 * 10**5

        k = gen_int(1, n - 1)
        res.append([n, k])

        a = [gen_int(0, 10**9) for _ in range(n)]
        res.append(a)

    return res
