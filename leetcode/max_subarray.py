# Find the contiguous subarray within an array (containing at least one
# number, with at least one number greater than 0) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def max_subarray_pos(self, arr):
        left = 0
        right = 0
        i = 0
        the_max = 0
        the_sum = 0
        for j in range(len(arr)):
            the_sum += arr[j]
            if the_sum < 0:
                the_sum = 0
                i = j + 1
            elif the_sum > the_max:
                the_max = the_sum
                left = i
                right = j
        return arr[left: right + 1]

    def max_subarray(self, arr):
        the_max = 0
        the_sum = 0
        for j in range(len(arr)):
            the_sum += arr[j]
            if the_sum < 0:
                the_sum = 0
            elif the_sum > the_max:
                the_max = the_sum
        return the_max


if __name__ == '__main__':
    the_arr = [2, 1, 4]
    obj = Solution()
    print(obj.max_subarray_pos(the_arr))
