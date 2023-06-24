from data.inputs_gen.dsl.dsl import INPUT_GENERATOR, gen_pos_int, record, gen_int


INPUT_GENERATOR


def generate_input():
    t = gen_pos_int(100)
    record(t)

    for _ in range(t):
        n = gen_int(3, 100)
        record(n)

        a = [gen_pos_int(100) for _ in range(n)]
        record(" ".join(map(str, a)))

        b = [gen_pos_int(100) for _ in range(n)]
        record(" ".join(map(str, b)))

        c = [gen_pos_int(100) for _ in range(n)]
        record(" ".join(map(str, c)))
