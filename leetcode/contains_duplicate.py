# Given an array of integers and an integer k, find out whether there are two
#  distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i, item in enumerate(nums):
            if table.get(item, None) is None:
                table[item] = i
            else:
                if i - table.get(item) <= k:
                    return True
                else:
                    table[item] = i
        return False
