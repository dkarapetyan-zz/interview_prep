# There are two sorted arrays A and B of size m and n respectively.
#
# Find the median of the two sorted arrays ( The median of the array formed
# by merging both the arrays ).
#
# The overall run time complexity should be O(log (m+n)).
#
# Sample Input
#
# A : [1 4 5]
# B : [2 3]
#
# Sample Output
#
# 3

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def __merge(self, A, B):
        final = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                final.append(A[i])
                i += 1
            else:
                final.append(B[j])
                j += 1
        if i == len(A) - 1:
            final.append(B[j:])
        elif j == len(B) - 1:
            final.append(A[i:])

    def findMedianSortedArrays(self, A, B):
