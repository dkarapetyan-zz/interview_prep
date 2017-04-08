from itertools import product
import numpy as np


class Solution(object):
    def _check_ones(self, matrix, corner1, corner2, history):
        """
        :param matrix: arr
        :param corner1: Tuple
        :param corner2: Tuple
        :param history: Dict
        :return: bool
        """
        arr = np.array(matrix)
        col_diff = corner2[1] - corner1[1]
        # base case
        if col_diff == 0:
            if matrix[corner1] == 1:
                history[hash((corner1, corner2))] = True
                if history['max'] < 1:
                    history['max'] = 1
                return True
            else:
                history[hash((corner1, corner2))] = False
                return False
        # recursive step

        smaller_square1 = self._check_ones(matrix,
                                           (corner1[0] + 1, corner1[1] + 1),
                                           (corner2[0], corner2[1]),
                                           history)
        smaller_square2 = self._check_ones(matrix,
                                           (corner1[0], corner1[1]),
                                           (corner2[0] - 1, corner2[1] - 1),
                                           history)
        smaller_square = smaller_square1 & smaller_square2

        if smaller_square is not None:
            if smaller_square is True:
                for i in range(col_diff):
                    if arr[corner1[0], corner1[1] + i] == 0 or arr[
                                corner1[0] + i, corner1[0]] == 0:
                        history[hash((corner1, corner2))] = False
                        return False
                if (col_diff + 1) ** 2 > history['max']:
                    history['max'] = (col_diff + 1) ** 2
                return True
            else:
                return False
        else:
            for i, j in product(
                    range(col_diff), range(col_diff)):
                if arr[i, j] == 0:
                    history[hash((corner1, corner2))] = False
                    return False
            history[hash((corner1, corner2))] = True
            return True

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        the_history = {'max': 0}
        arr = np.array(matrix)
        self._check_ones(arr, (0, 0),
                         (arr.shape[0] - 1, arr.shape[1] - 1),
                         the_history)
        return the_history['max']


if __name__ == '__main__':
    the_matrix = np.ones((6, 6))
    the_matrix[0, 1] = 0
    # the_matrix[3, 4] = 0
    obj = Solution()
    print(obj.maximalSquare(the_matrix))
