def bit_insert(n, m, i, j):
    left_ones = ~0 - ((1 << j) - 1)
    right_ones = (1 << i) - 1
    mask = left_ones | right_ones
    n_zeroes_middle = n & mask
    return (m << i) | n_zeroes_middle


if __name__ == '__main__':
    print(bit_insert(21, 3, 2, 3))
