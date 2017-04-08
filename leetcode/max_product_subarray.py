# Find the contiguous subarray within an array (containing at least one
# number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def max_prodarray(self, arr):
        max_ending_here = 1
        min_ending_here = 1
        max_so_far = arr[0]
        # min and max because the max_ending_here or min_ending_here may
        # be 0, i.e. they may not_exist
        # for j-1th position
        for j in range(len(arr)):
            if arr[j] > 0:
                max_ending_here = max(max_ending_here * arr[j], arr[j])
                min_ending_here = min(min_ending_here * arr[j], arr[j])
            elif arr[j] == 0:
                max_ending_here = min_ending_here = 0
            else:
                temp = max_ending_here
                max_ending_here = max(min_ending_here * arr[j], arr[j])
                min_ending_here = min(temp * arr[j], arr[j])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


if __name__ == '__main__':
    arr = [0]
    obj = Solution()
    print obj.max_prodarray(arr)
