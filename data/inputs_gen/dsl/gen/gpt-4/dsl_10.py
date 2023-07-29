from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(2 * 10**4)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_int(2, 10**5)
        res.append(n)
        list_n.append(n)

        p = [gen_pos_int(n) for _ in range(n)]
        res.append(p)

        assert all_elements_unique(p)

    assert sum(list_n) <= 10**5

    return res
