from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *




def generate_input() -> list:
    t = gen_pos_int(10**3)
    res = [t]
    for _ in range(t):
        d = gen_int(0, 10**3)
        res.append(d)

    return res

