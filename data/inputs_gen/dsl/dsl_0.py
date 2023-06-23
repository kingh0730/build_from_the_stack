from dsl import integer, enum, concat_str, record


def generate_input():
    t = integer(1, 10**4)
    record(t)

    for _ in range(t):
        n = integer(1, 2 * 10**5)
        record(n)

        for _ in range(n):
            word_length = integer(1, 4 * 10**6 // n)
            word = concat_str(*[enum("0", "1") for _ in range(word_length)])
            record(word)
