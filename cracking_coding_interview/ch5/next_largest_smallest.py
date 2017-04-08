def _lowest_one_bit(n):
    i = 0
    m = n
    while m % 2 != 1:
        i += 1
        m /= 2

    return i


def _next_smallest(n):
    loc = _lowest_one_bit(n)
    final = n - (1 << loc) + 1 << (loc - 1)
    return final
