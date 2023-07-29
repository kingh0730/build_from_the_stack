from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *



def generate_input() -> list:
    t = gen_pos_int(200)
    res = [t]
    for _ in range(t):
        n = gen_pos_int(200) * 2
        res.append(n)

    return res
    
