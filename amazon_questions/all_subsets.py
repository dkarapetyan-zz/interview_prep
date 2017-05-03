# Given a set of distinct integers, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
# Example :
#
# If S = [1,2,3], a solution is:
#
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]
from copy import deepcopy


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def _helper(self, index, A):
        if index < 0:
            return [[]]
        output = self._helper(index - 1, A)
        output_copy = deepcopy(output)
        for item in output_copy:
            item.append(A[index])
        output.extend(output_copy)
        return output

    def subsets(self, A):
        A.sort()
        output = self._helper(len(A) - 1, A)
        output.sort()
        return output


if __name__ == '__main__':
    OBJ = Solution()
    THE_ARRAY = [1, 2, 3]
    print(OBJ.subsets(THE_ARRAY))
