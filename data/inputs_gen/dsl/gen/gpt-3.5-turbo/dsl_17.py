from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *



def generate_input() -> list:
    res = []

    t = gen_pos_int(100)
    res.append(t)

    for _ in range(t):
        n = gen_int(4, 3000)
        res.append(n)

        a = [gen_pos_int(n) for _ in range(n)]
        res.append(a)

    return res

