from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *





def generate_input() -> list:
    t = gen_pos_int(10**4)
    res = [t]
    for _ in range(t):
        a1 = gen_pos_int(100)
        b1 = gen_pos_int(100)
        res.append([a1, b1])

        a2 = gen_pos_int(100)
        b2 = gen_pos_int(100)
        res.append([a2, b2])

        if choice([True, False]):  # 50% chance to generate a valid input
            if a1 == a2:
                assert b1 + b2 == a1
            elif a1 == b2:
                assert b1 + a2 == a1
            elif b1 == a2:
                assert a1 + b2 == b1
            elif b1 == b2:
                assert a1 + a2 == b1
        else:
            assert (
                (a1 != a2 or b1 + b2 != a1)
                and (a1 != b2 or b1 + a2 != a1)
                and (b1 != a2 or a1 + b2 != b1)
                and (b1 != b2 or a1 + a2 != b1)
            )

    return res

