class Solution(object):
    def _swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums) - 1):
                    self._swap(nums, j, j + 1)


if __name__ == '__main__':
    obj = Solution()
    bobo = [0, 0, 1]
    obj.moveZeroes(bobo)
    print(bobo)
