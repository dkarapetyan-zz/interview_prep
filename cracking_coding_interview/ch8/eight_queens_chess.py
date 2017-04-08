from copy import copy
import numpy as np


def _clash_in_column(i, j, matrix):
    for k in range(i + 1):
        if matrix[k][j] != 0:
            return True
    return False


def _clash_in_row(i, j, matrix):
    for k in range(8):
        if matrix[i][k] != 0:
            return True
    return False


def _clash_in_diag(i, j, array):
    for k in range(min(i, j) + 1):
        if array[i - k, j - k] == 1:
            return True
        if j + k < 8:
            if array[i - k, j + k] == 1:
                return True
    return False


def _not_attack(i, j, matrix):
    if _clash_in_column(i, j, matrix) or _clash_in_row(i, j, matrix) or \
            _clash_in_diag(i, j, matrix):
        return False
    return True


def queen_arrange(row_num):
    if row_num == 0:
        return [np.zeros((8, 8))]
    else:
        solutions = []
        list_of_matrices = queen_arrange(row_num - 1)
        for matrix in list_of_matrices:
            for j in range(8):
                if _not_attack(row_num - 1, j, matrix):
                    matrix_copy = copy(matrix)
                    matrix_copy[row_num - 1, j] = 1
                    solutions.append(matrix_copy)
    return solutions


if __name__ == '__main__':
    result = queen_arrange(8)
    print(result)
