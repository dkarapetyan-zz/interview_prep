# Given a set of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ak) must be in non-descending order.
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR (a1
#  = b1 AND a2 = b2 AND ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:
#
# [2, 2, 3]
# [7]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you
# penalty points.


from copy import deepcopy
import itertools


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum1(self, A, B):
        storage = {i: [] for i in range(1, B + 1)}
        for i in range(1, B + 1):
            for j in reversed(range(1, i)):
                # if i % j == 0:
                #     storage[i].append([j] * (i / j))
                if storage[j] != []:
                    diff = i - j
                    if diff in A:
                        arr = deepcopy(storage[j])
                        for item in arr:
                            if diff >= item[-1]:
                                item.append(diff)
                            else:
                                item.insert(0, diff)
                        storage[i].extend(arr)
            if i in A:
                storage[i].append([i])
            if len(storage[i]) == 0:
                storage[i] = []
        if storage[B] == []:
            return []
        else:
            storage[B].sort()
            final = [k for k, _ in itertools.groupby(storage[B])]
            return final

    # can use dfs approach to avoid sorting of final result, but doesn't
    # change complexity of algorithm
    def _combinationSum(self, index, A, B):
        storage = []
        # base case
        if B == 0:
            return [[]]
        elif B < 0:
            return None
        # inductive step
        for i in range(index + 1):
            output = self._combinationSum(i, A, B - A[i])
            if output is not None:
                for elem in output:
                    elem.append(A[i])
                storage.extend(output)
        return storage

    def combinationSum(self, A, B):
        return self._combinationSum(len(A) - 1, A, B)


if __name__ == '__main__':
    obj = Solution()
    the_array = [1, 3, 7, 20]
    the_array.sort()
    final = obj.combinationSum(the_array, 14)
    final.sort()
    print(final)
