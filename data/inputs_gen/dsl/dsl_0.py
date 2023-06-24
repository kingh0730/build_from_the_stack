from dsl import gen_pos_int, enum, record, to_str_then_concat


def generate_input():
    t = gen_pos_int(10**4)
    record(t)

    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        record(n)

        for _ in range(n):
            word_length = gen_pos_int(4 * 10**6 // n)
            word = to_str_then_concat(
                [enum("0", "1") for _ in range(word_length)],
            )
            record(word)
