# Given a list of non negative integers, arrange them such that they form the
#  largest number.
#
# For example:
#
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead
# of an integer.

class Solution:
    # @param A : tuple of integers
    # @return a strings

    # pad the end with the last element
    def _cmp(self, string1, string2):
        if string1 + string2 > string2 + string1:
            return -1
        elif string1 + string2 == string2 + string1:
            return 0
        else:
            return 1

    def largestNumber(self, A):
        new_list = [str(item) for item in A]
        largest_num = max(A)
        indices = 0
        while largest_num > 0:
            largest_num /= 10
            indices += 1

        sorted_list = new_list
        sorted_list = list(sorted(sorted_list, cmp=self._cmp))
        final_string = "".join(sorted_list)

        if final_string[0] == '0':
            return '0'
        else:
            return final_string


if __name__ == '__main__':
    obj = Solution()
    print(obj.largestNumber([8, 89]))
