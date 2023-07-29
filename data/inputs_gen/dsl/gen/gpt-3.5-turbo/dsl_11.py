from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *




def generate_input() -> list:
    T = gen_pos_int(1000)
    res = [T]
    for _ in range(T):
        s = "".join([choice(["W", "A", "S", "D"]) for _ in range(gen_pos_int(2 * 10**5))])
        res.append(s)

    return res

