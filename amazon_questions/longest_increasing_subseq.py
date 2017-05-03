# Find the longest increasing subsequence of a given sequence / array.

# In other words, find a subsequence of array in which the subsequence
# elements are in strictly increasing order, and in which the subsequence is
# as long as possible.
# This subsequence is not necessarily contiguous, or unique.
# In this case, we only care about the length of the longest increasing
# subsequence.
#
# Example :
#
# Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output : 6
# The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9,
#  13, 15]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        storage = [1]
        for i in range(1, len(A)):
            max_so_far = 1
            for j in reversed(range(i)):
                if A[j] < A[i]:
                    if storage[j] >= max_so_far:
                        max_so_far = storage[j] + 1
            storage.append(max_so_far)

        return max(storage)


if __name__ == '__main__':
    obj = Solution()
    print(obj.lis([69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82,
                   65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35, 101, 44,
                   74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17, 54, 89,
                   93, 10, 7, 88, 68, 10, 11, 22, 25, 50, 18, 59, 79, 87, 7,
                   49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94,
                   60, 27, 76, 4, 43, 66, 14, 8, 78, 72, 21, 56, 34, 90, 89]
                  ))
