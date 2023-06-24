from dsl import gen_pos_int, record, INPUT_GENERATOR, to_str_then_concat_with_space


INPUT_GENERATOR


def generate_input():
    q = gen_pos_int(10**4)
    record(q)

    for _ in range(q):
        ni = gen_pos_int(10**18)
        mi = gen_pos_int(10**18)
        ki = gen_pos_int(10**18)

        line = to_str_then_concat_with_space([ni, mi, ki])
        record(line)
