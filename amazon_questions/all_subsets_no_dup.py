# Given a collection of integers that might contain duplicates, S, return all
#  possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:
#
# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]

from copy import deepcopy
import itertools


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def _helper(self, index, A):
        if index < 0:
            return [[]]
        output = self._helper(index - 1, A)
        final = deepcopy(output)
        for item in output:
            item.append(A[index])
        final.extend(output)
        return final

    def subsetsWithDup(self, A):
        A.sort()
        final = self._helper(len(A) - 1, A)
        final.sort()
        the_final = [item for item, _ in itertools.groupby(final)]
        return the_final


if __name__ == '__main__':
    obj = Solution()
    the_array = [1, 2, 2, 3]
    print(obj.subsetsWithDup(the_array))
