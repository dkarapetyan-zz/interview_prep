def rep_n_cents(n, array_denoms):
    array_denoms.sort()
    denom = array_denoms[-1]
    if denom == 1:
        return 1
    else:
        new_array = array_denoms[:-1]

    ways = 0
    for i in range(n / denom + 1):
        ways += rep_n_cents(n - i * denom, new_array)
    return ways


if __name__ == '__main__':
    print(rep_n_cents(50, [10, 25, 5, 1]))
