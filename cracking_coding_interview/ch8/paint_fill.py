import numpy as np


def paint_fill_fin(array, m, n, color):
    paint_fill(array, m, n, color)
    array[m, n] = color


def paint_fill(array, m, n, color):
    if m >= len(array) or n >= len(array[0]) or m < 0 or n < 0:
        return
    else:
        if m + 1 < len(array):
            if array[m + 1, n] == array[m, n]:
                array[m + 1, n] = color
                paint_fill(array, m + 1, n, color)
        if m - 1 >= 0:
            if array[m - 1, n] == array[m, n]:
                array[m - 1, n] = color
                paint_fill(array, m - 1, n, color)
        if n + 1 < len(array[0]):
            if array[m, n + 1] == array[m, n]:
                array[m, n + 1] = color
                paint_fill(array, m, n + 1, color)
        if n - 1 >= 0:
            if array[m, n - 1] == array[m, n]:
                array[m, n - 1] = color
                paint_fill(array, m, n - 1, color)


if __name__ == '__main__':
    the_array = np.array([['blue', 'blue', 'blue'], ['green', 'green', 'cyan']])
    paint_fill_fin(the_array, 1, 1, 'yellow')
    print(the_array)
