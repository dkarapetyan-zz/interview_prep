class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = 0
        for i in xrange(0, len(nums), 2):
            max1 += nums[i]
        for j in xrange(1, len(nums), 2):
            max2 += nums[j]

        return max(max1, max2)


if __name__ == '__main__':
    arr = [1, 2]
    obj = Solution()
    print(obj.rob(arr))
