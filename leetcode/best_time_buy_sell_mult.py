# Say you have an array for which the 'i'th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at
# the same time (i.e, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


if __name__ == '__main__':
    arr = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]
    obj = Solution()
    print(obj.maxProfit(arr))
