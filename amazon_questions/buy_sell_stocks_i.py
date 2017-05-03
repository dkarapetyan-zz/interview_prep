# Say you have an array for which the ith element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one
#  and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Example :
#
# Input : [1 2]
# Return :  1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 2:
            return 0

        the_min = A[0]
        max_profit = 0
        storage = [0]
        for i in range(1, len(A)):
            if A[i] < the_min:
                the_min = A[i]
            max_profit = max(max_profit, storage[i - 1], A[i] - the_min)
            storage.append(max_profit)
        return storage[-1]
