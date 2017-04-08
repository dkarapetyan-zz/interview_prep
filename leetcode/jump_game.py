# Given an array of non-negative integers, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution(object):
    # recursive solution. Causes stack overflow for some crazy long input
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self._can_jump(nums, 0, {})

    def _can_jump(self, nums, i, history):
        # base case
        if i == len(nums) - 1:
            return True
        elif nums[i] == 0:
            return False
        # recursive step
        for j in range(i + 1, i + nums[i] + 1):
            if history.get(j, None) is None:
                if self._can_jump(nums, j, history):
                    history[j] = True
                    return True
                else:
                    history[j] = False
            else:
                return history.get(j)

        return False

    # iterative approach
    def canJump(self, nums):
        last = len(nums) - 1
        i = last - 1
        first_true = last
        while i >= 0:
            if nums[i] >= first_true - i:
                first_true = i
            i -= 1
        if first_true == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = Solution()
    arr = [0, 1]
    print(obj.canJump(arr))
