from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *




def generate_input() -> list:
    T = gen_pos_int(1000)
    res = [T]
    total_s_len = 0
    for _ in range(T):
        s_len = gen_pos_int(2 * 10**5)
        total_s_len += s_len

        s = "".join([choice(["W", "A", "S", "D"]) for _ in range(s_len)])
        res.append(s)

    assert total_s_len <= 2 * 10**5

    return res

