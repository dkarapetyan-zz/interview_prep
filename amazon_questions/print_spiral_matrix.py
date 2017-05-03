class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers

    def _outer_ring(self, A, tl_row, tl_col, br_row, br_col, storage):
        for j in range(tl_col, br_col + 1):
            storage.append(A[tl_row][j])

        for i in range(1 + tl_row, br_row + 1):
            storage.append(A[i][br_col])

        for j in reversed(range(tl_col, br_col)):
            storage.append(A[br_row][j])

        for i in reversed(range(tl_row + 1, br_row)):
            storage.append(A[i][tl_col])

        return tl_row + 1, tl_col + 1, br_row - 1, br_col - 1, storage

    def _spiralOrder(self, A, storage):
        tl_row, tl_col, br_row, br_col = 0, 0, len(A) - 1, len(A[0]) - 1

        while br_row >= tl_row and br_col >= tl_col:
            tl_row, tl_col, br_row, br_col, storage = self._outer_ring(A,
                                                                       tl_row,
                                                                       tl_col,
                                                                       br_row,
                                                                       br_col,
                                                                       storage)

        return storage

    def spiralOrder(self, A):
        print(self._spiralOrder(A, []))


if __name__ == '__main__':
    obj = Solution()
    obj.spiralOrder([[1, 2, 4], [3, 4, 8], [5, 6, 9]])
