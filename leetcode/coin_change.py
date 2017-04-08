class Solution(object):
    # use memoization
    # not fast enough for leetcode--could just be bug with leetcode
    def _coinChange3(self, coins, amount, table):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # base case
        if amount == 0:
            return 0

        if len(coins) == 0 or amount < 0:
            return -1

        # inductive step
        storage = []
        for i in reversed(range(amount / coins[-1] + 1)):
            the_hash = hash((tuple(coins[0:-1]), amount - i * coins[-1]))
            y = table.get(the_hash, None)
            if y is None:
                y = self._coinChange(coins[0:-1], amount - i * coins[-1], table)
                table[the_hash] = y
            if y != -1:
                storage.append(y + i)
        new_hash = hash((tuple(coins), amount))
        table[new_hash] = min(storage) if len(storage) != 0 else -1
        return table[new_hash]

    # alt implementation--sped up version where hash table uses less memory.
    # solution in online forums as well--leetcode still complains it is too
    # slow.
    # moving on
    def _coinChange2(self, coins, amount, table):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # base case
        if amount == 0:
            return 0

        if amount < 0:
            return -1

        # inductive step
        the_min = None
        for coin in reversed(coins):
            the_hash = hash(amount - coin)
            y = table.get(the_hash, None)
            if y is None:
                y = self._coinChange(coins, amount - coin, table)
                table[the_hash] = y
            if y != -1:
                if the_min is None:
                    the_min = y + 1
                elif y + 1 < the_min:
                    the_min = y + 1
        new_hash = hash(amount)
        table[new_hash] = the_min if the_min is not None else -1
        return table[new_hash]

    # iterative solution--the answer. Overhead of recursive stack in previous
    # implementations caused algo to fail on leetcode, along with some
    # inefficiency of memoization--may not have a result in table
    # that we need when recursing, since order that we recurse in may not
    # be optimal
    def _coinChange(self, coins, amount, table):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # initialize
        table[hash(0)] = 0
        # iterative loop (counterpart to recursive step)
        for am in range(1, amount + 1):
            storage = [table.get(hash(am - coin), None) for coin in coins if
                       table.get(hash(am - coin), None) >= 0]
            table[hash(am)] = min(storage) + 1 if len(storage) > 0 else -1
        return table[hash(amount)]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self._coinChange3(coins, amount, table={})


if __name__ == '__main__':
    coins = [3, 7, 405, 436]
    amount = 8839
    #    amount = 3
    obj = Solution()
    print(obj.coinChange(coins, amount))
