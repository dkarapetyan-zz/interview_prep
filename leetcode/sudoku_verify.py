import itertools
import numpy as np


def sudoku_ok(line, length):
    return len(line) == length and sum(line) == sum(set(line))


def sudoku_ok_square(square, length):
    bad_rows = [row for row in square if not sudoku_ok(row, length)]
    bad_cols = [row for row in np.transpose(square) if not sudoku_ok(row,
                                                                     length)]
    return not (bad_rows or bad_cols)


def check_sudoku(grid):
    grid = np.array(grid)
    bad_rows = [row for row in grid if not sudoku_ok(row, 9)]
    bad_cols = [col for col in np.transpose(grid) if not sudoku_ok(col, 9)]
    # now check individual 3x3 boxes
    squares = []
    for i, j in itertools.product(range(9, step=3), range(9, step=3)):
        square = grid[i:i + 3, j:j + 3]
        squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square, 3)]
    return not (bad_rows or bad_cols or bad_squares)
