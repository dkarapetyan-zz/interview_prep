# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        i = 0
        final = []
        for j in range(1, len(nums)):
            if nums[j] - nums[i] != j - i:
                if i != j - 1:
                    final.append("{}->{}".format(nums[i], nums[j - 1]))
                else:
                    final.append("{}".format(nums[i]))
                if j == len(nums) - 1:
                    final.append("{}".format(nums[j]))
                    break
                i = j
            elif j == len(nums) - 1:
                final.append("{}->{}".format(nums[i], nums[j]))

        return final


if __name__ == '__main__':
    obj = Solution()
    arr = [0, 1, 2, 3, 5, 6, 8, 10]
    print(obj.summaryRanges(arr))
