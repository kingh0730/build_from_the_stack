from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


def generate_input() -> list:
    t = gen_pos_int(10**4)
    res = [t]
    total_n = 0
    for _ in range(t):
        n = gen_pos_int(2 * 10**5 - total_n)
        total_n += n
        res.append(n)

        perm = list(range(1, n))
        random.shuffle(perm)

        l1 = gen_pos_int(n - 1)
        l2 = n - l1

        p1 = sorted(perm[:l1])
        p2 = sorted(perm[l1:])

        a = p1 + p2
        random.shuffle(a)

        res.append(a)

    assert total_n < 2 * 10**5

    return res
