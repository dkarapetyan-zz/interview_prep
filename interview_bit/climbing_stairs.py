# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Example :
#
# Input : 3
# Return : 3
#
# Steps : [1 1 1], [1 2], [2 1]

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        hash_table = {0: 1, 1: 1}
        i = 0
        while i <= A:
            if hash_table.get(i, None) is None:
                hash_table[i] = hash_table[i - 1] + hash_table[i - 2]
            i += 1

        return hash_table[A]
