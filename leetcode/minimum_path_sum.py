# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

import numpy as np
from itertools import product


class Solution(object):
    # time limit exceeded for Leetcode. Iterative approach will be faster
    # than recursive with memoization
    def _minPathSum2(self, grid, (k, l), table):
        # base case:
        if (k, l) == (0, 0):
            return grid[0][0]

        if k < 0 or l < 0:
            return float('inf')
        # initialize table
        table[hash((0, 0))] = grid[0][0]
        for i in range(1, len(grid[0])):
            table[hash((0, i))] = table.get(hash((0, i - 1))) + grid[0][i]

        for i in range(1, len(grid)):
            table[hash((i, 0))] = table.get(hash((i - 1, 0))) + grid[i][0]

        # populate table recursively via memoization
        if table.get(hash((k, l - 1)), None) is None:
            x = self._minPathSum(grid, (k, l - 1), table)
            table[hash((k, l - 1))] = x
        if table.get(hash((k - 1, l)), None) is None:
            y = self._minPathSum(grid, (k - 1, l), table)
            table[hash((k - 1, l))] = y
        return grid[k][l] + min(
            table[hash((k, l - 1))],
            table[hash((k - 1, l))])

    def _minPathSum(self, grid, (k, l), table):
        # base case:
        # initialize first row and first column of table
        table[hash((0, 0))] = grid[0][0]
        for i in range(1, len(grid[0])):
            table[hash((0, i))] = table[hash((0, i - 1))] + grid[0][i]

        for i in range(1, len(grid)):
            table[hash((i, 0))] = table[hash((i - 1, 0))] + grid[i][0]

        # populate rest of table

        for i, j in product(range(1, len(grid)), range(1, len(
                grid[0]))):
            table[hash((i, j))] = min(table[hash((i, j - 1))],
                                      table[hash((i - 1, j))]) + grid[i][j]
        return table[hash((k, l))]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        return self._minPathSum(grid, (rows - 1, cols - 1), {})


if __name__ == '__main__':
    the_matrix = np.random.randint(0, 2, size=(7, 7))
    obj = Solution()
    print obj.minPathSum(the_matrix)
    print(the_matrix)
