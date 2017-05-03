class Solution:
    # @param A : integer
    # @return an integer
    def _sqrt(self, A, left, right):
        if A == 0 or A == 1:
            return A
        elif left ** 2 == A or \
                (int(left) ** 2 < A and ((int(left) + 1) ** 2) > A):
            return int(left)
        elif left ** 2 > A:
            new_right = left
            new_left = left / float(2)
            return self._sqrt(A, new_left, new_right)
        else:
            new_left = (left + right) / float(2)
            return self._sqrt(A, new_left, right)

    def sqrt(self, A):
        return self._sqrt(A, 1, A / float(2))


if __name__ == '__main__':
    obj = Solution()
    print(obj.sqrt(145621280))
