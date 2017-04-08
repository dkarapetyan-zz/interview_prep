# Say you have an array for which the ith element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one
#  and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
#  than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                max_profit = max(max_profit, price - lowest)
        return max_profit

    # o(n^2). Too slow for leetcode
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_val = 0
        i = 0
        while i < len(prices):
            for price in prices[i + 1:]:
                max_val = max(max_val, price - prices[i])
            i += 1
        return max_val


if __name__ == '__main__':
    input = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print(obj.maxProfit(input))
