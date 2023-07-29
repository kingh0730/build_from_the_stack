from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *



def generate_input() -> list:
    t = gen_pos_int(1024)
    res = [t]
    list_n = []
    for _ in range(t):
        n = gen_pos_int(1024)
        res.append(n)
        list_n.append(n)

        S = [gen_int(0, 1023) for _ in range(n)]
        assert all_elements_unique(S)
        res.append(S)

    assert sum(list_n) <= 1024

    return res
