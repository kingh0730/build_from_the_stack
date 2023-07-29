from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(10000)
    res = [t]
    total_n = 0
    for _ in range(t):
        n = gen_pos_int(10**5)
        total_n += n
        assert total_n <= 10**5

        res.append(n)

        a = [choice([-1, 0, 1]) for _ in range(n)]
        res.append(a)

        b = [gen_int(-10**9, 10**9) for _ in range(n)]
        res.append(b)

    return res
