def robot_walk(i, j, m, n, forbidden_i, forbidden_j):
    # base case
    if i == forbidden_i and j == forbidden_j:
        return 0
    else:
        if m == 1 or n == 1:
            if m == 1 and n != 1 or m != 1 and n == 1:
                return 1
            else:
                return 0
    # inductive step
    return robot_walk(i + 1, j, m - 1, n, forbidden_i, forbidden_j) + \
           robot_walk(i, j - 1, m, n - 1, forbidden_i, forbidden_j)


if __name__ == '__main__':
    m, n = map(int,
               raw_input("Enter two numbers, separated by a comma:").split(','))
    print(robot_walk(0, n - 1, m, n, m - 2, n - 2))
