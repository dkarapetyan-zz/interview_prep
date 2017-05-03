# Say you have an array for which the ith element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most
# two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
# Example :
#
# Input : [1 2 1 2]
# Output : 2
#
# Explanation :
#   Day 1 : Buy
#   Day 2 : Sell
#   Day 3 : Buy
#   Day 4 : Sell

# the description of the algorithm is inaccurate. It doesn't match what the
# codes really do.
#
# //   f[k][i] : k transactions ENDs with prices[i]
# //   f[k][i] = max(f[k][i - 1], f[k - 1][j] + prices[i] - prices[j]))
#     //j = 0..i-1
# //=> f[k][i] = max(f[k][i - 1], prices[i] + max(f[k - 1][j] - prices[j]))
#     //j = 0..i-1
# //temp = max(f[k - 1][j] - prices[j]);



class Solution:
    # @param A : tuple of integers
    # @return an integer

    # linear time, due to trick of keeping track of maximum without need of
    # inner
    # loop
    def maxProfit(self, A):
        if len(A) == 0:
            return 0

        storage = {0: [0] * len(A), 1: [0], 2: [0]}
        max_so_far = 0
        for k in [1, 2]:
            temp = storage[k][0] - A[0]
            for i in range(len(A)):
                temp = max(temp, storage[k - 1][i] - A[i])
                max_so_far = max(max_so_far, storage[k][i], temp + A[i])
                storage[k].append(max_so_far)

        return storage[2][-1]

    # quadratic time
    def maxProfit_sub(self, A):
        storage = {0: [0] * len(A), 1: [0], 2: [0]}
        max_so_far = 0
        for k in [1, 2]:
            for i in range(len(A)):
                for j in range(i):
                    max_so_far = max(max_so_far,
                                     storage[k][i], storage[k - 1][j] +
                                     A[i] - A[j])
                storage[k].append(max_so_far)

        return storage[2][-1]


if __name__ == '__main__':
    obj = Solution()
    # 1, 2, 10, 12, 0, 5, 12, 1, 2
    print(obj.maxProfit([2, 1, 13, 4, 2, 20, 17]))
    # print(obj.maxProfit([2, 1]))
