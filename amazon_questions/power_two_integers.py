# Power Of Two IntegersBookmark Suggest Edit
# Given a positive integer which fits in a 32 bit signed integer, find if it
# can be expressed as A^P where P > 1 and A > 0. A and P both should be
# integers.
#
# Example
#
# Input : 4
# Output : True
# as 2^2 = 4.

class Solution:
    # @param A : integer
    # @return a boolean

    def isPower(self, A):
        if A == 1:
            return True
        for i in range(2, 32):
            output = A ** (1. / i)
            output_low = int(output) ** i
            output_high = (int(output) + 1) ** i
            if output_low == A or output_high == A:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isPower(4))
