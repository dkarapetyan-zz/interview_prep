class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 1
        length = len(nums)
        while i < length:
            if nums[i] == nums[i - 1]:
                del nums[i]
                length -= 1
            else:
                i += 1
        return length


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([1, 2, 2, 2]))
