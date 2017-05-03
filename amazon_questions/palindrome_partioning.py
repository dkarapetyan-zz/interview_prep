# Given a string s, partition s such that every substring of the partition is
#  a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example :
# Given
# s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced
# using 1 cut.
class Solution:
    # @param A : string
    # @return an integer

    def _is_palindrome(self, A, i, j):
        return A[i: j + 1] == list(reversed(A[i: j + 1]))

    def _minCut(self, A, i, j, storage):
        # testing
        if i > j:
            raise ValueError("i must be less than or equal to j")
        if j > len(A) - 1:
            raise ValueError("j exceeds the largest index of A")
        if len(A) == 0:
            return 0

        # main code
        min_so_far = float('inf')
        if self._is_palindrome(A, i, j):
            storage[i][j] = 0
        else:
            for L in range(2, j - i + 1):
                for k in range(i, j - L + 2):  # possible starting indices for #
                    #  substrings of length L
                    for m in range(L - 1):
                        min_so_far = min(min_so_far, storage[k][k + m] + 1 +
                                         storage[k + m + 1][k + L - 1])
                    storage[k][k + L - 1] = min_so_far
        return storage[i][j]

    def minCut(self, A):
        storage = [[None for item in A] for item in A]
        for j in range(len(A)):
            storage[j][j] = 0
        for i in range(len(A)):
            self._minCut(A, i, len(A) - 1, storage)
        return storage[0][len(A) - 1]


if __name__ == '__main__':
    obj = Solution()
    A = "abc"
    print(obj.minCut(A))
