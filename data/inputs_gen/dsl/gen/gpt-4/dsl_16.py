from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *



def generate_input() -> list:
    tc = gen_pos_int(20)
    res = [tc]
    for _ in range(tc):
        n = gen_pos_int(100)
        res.append(n)

        C = round(gen_float(0.001, 9.999), 3)
        T = round(gen_float(0, 2 * 10**5), 3)
        res.append([C, T])

        for _ in range(n):
            a_i = gen_pos_int(10**4)
            p_i = gen_pos_int(10)
            res.append([a_i, p_i])

    return res

