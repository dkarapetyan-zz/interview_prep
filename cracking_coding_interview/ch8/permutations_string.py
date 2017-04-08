def swap(i, j, my_string):
    x = list(my_string)
    x[i], x[j] = x[j], x[i]
    return "".join(x)


def permutations(my_string, start, end):
    if start == end:
        yield my_string
    else:
        perms = list(permutations(my_string, start + 1, end))
        for i in range(end - start + 1):
            for item in perms:
                yield swap(i, start + 1, item)


if __name__ == '__main__':
    print(list(permutations('cap', 0, 2)))
