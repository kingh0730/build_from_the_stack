from dsl_impl import (
    gen_pos_int,
    choice,
    to_str_then_concat,
    all_elements_unique,
    GENERATE_INPUT,
)


GENERATE_INPUT


def generate_input() -> list:
    res = []

    t = gen_pos_int(10**4)
    res.append(t)

    list_n = []
    list_word_len_all_test_cases = []
    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        res.append(n)
        list_n.append(n)

        list_word_len_this_test_case = []
        list_word = []
        for _ in range(n):
            word_len = gen_pos_int(4 * 10**6)
            list_word_len_this_test_case.append(word_len)

            word = to_str_then_concat(
                [choice(["0", "1"]) for _ in range(word_len)],
            )
            res.append(word)

        assert sum(list_word_len_this_test_case) <= 4 * 10**6
        assert all_elements_unique(list_word)

    assert sum(list_n) <= 2 * 10**5
    assert sum(list_word_len_all_test_cases) <= 4 * 10**6
