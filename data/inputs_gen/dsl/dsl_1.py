from dsl import gen_pos_int, record, INPUT_GENERATOR


INPUT_GENERATOR


def generate_input():
    q = gen_pos_int(10**4)
    record(q)

    for _ in range(q):
        ni = gen_pos_int(10**18)
        mi = gen_pos_int(10**18)
        ki = gen_pos_int(10**18)
        record(ni)
        record(mi)
        record(ki)
