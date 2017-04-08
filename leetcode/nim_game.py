# You are playing the following Nim Game with your friend: There is a heap of
#  stones on the table, each time one of you take turns to remove 1 to 3
# stones. The one who removes the last stone will be the winner. You will
# take the first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for the game. Write
#  a function to determine whether you can win the game given the number of
# stones in the heap.
#
# For example, if there are 4 stones in the heap, then you will never win the
#  game: no matter 1, 2, or 3 stones you remove, the last stone will always
# be removed by your friend.
#
# Show Hint


from itertools import islice, count


class Solution(object):
    # maximum recursion depth reached. Python sucks for recursion
    def _canWinNim(self, n, table):
        """
        :type n: int
        :rtype: bool
        """
        if n in [1, 2, 3]:
            return True

        if n == 4:
            return False

        for i in [n - 1, n - 2, n - 3]:
            if table.get(i, None) is None:
                table[i] = self._canWinNim(i, table)

        return not (
            table[n - 1] and table[n - 2] and table[n - 3])

    def canWinNim2(self, n):
        return self._canWinNim(n, {})

    # iterative approach with hash table--but memory efficient (o(1)) table.
    # Do this by discarding entries we no longer need
    # Still fails with a time limit exceeded on leetcode
    def canWinNim3(self, n):
        # initialize table

        table = [True for i in range(3)]

        # inductive step
        for i in islice(count(3), n + 1):
            table.append(not (table[0] and table[1] and table[2]))
            table.pop(0)

        return table[-1]

    def canWinNim(self, n):
        return n % 4 != 0


if __name__ == '__main__':
    obj = Solution()
    print(obj.canWinNim(8))
