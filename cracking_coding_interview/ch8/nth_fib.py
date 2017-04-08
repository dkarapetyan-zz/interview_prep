def nth_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return nth_fib(n - 1) + nth_fib(n - 2)


if __name__ == '__main__':
    x = input()
    print(nth_fib(x))
