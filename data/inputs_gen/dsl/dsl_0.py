from dsl import (
    gen_pos_int,
    enum,
    record,
    to_str_then_concat,
    all_elements_unique,
    GENERATE_INPUT,
)


GENERATE_INPUT


def generate_input():
    t = gen_pos_int(10**4)
    record(t)

    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        record(n)

        all_word_length = []
        all_word = []

        for _ in range(n):
            word_length = gen_pos_int(4 * 10**6 // n)
            all_word_length.append(word_length)

            word = to_str_then_concat(
                [enum("0", "1") for _ in range(word_length)],
            )
            all_word.append(word)

            record(word)

        assert sum(all_word_length) <= 4 * 10**6
        assert all_elements_unique(all_word)
