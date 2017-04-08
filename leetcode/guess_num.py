# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        elif guess(n) == -1:
            if guess(n / 2) == 0:
                return n / 2
            elif guess(n / 2) == -1:
                return self.guessNumber(n / 2)
            else:
                return self.guessNumber(3 * n / 4)
        else:
            if guess(2 * n) == 0:
                return 2 * n
            elif guess(2 * n) == -1:
                return self.guessNumber(3 * n / 2)
            else:
                return self.guessNumber(2 * n)
