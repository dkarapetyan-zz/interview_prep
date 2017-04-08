# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
#  returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution(object):
    # o(n\log n) complexity

    def dis_num_first(self, nums):
        nums.sort()
        holder = []
        for item in range(1, len(nums)):
            if item in nums:
                holder.append(item)
        return holder

    # o(n) complexity, o(n) space
    def dis_num_second(self, nums):
        hash_table = {}
        ans = []
        for i in nums:
            if hash_table.get(i, None) is None:
                hash_table[i] = -1

        for i in range(1, len(nums) + 1):
            if hash_table.get(i, None) is None:
                ans.append(i)

        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.dis_num_second([4, 3, 2, 7, 8, 2, 3, 1]))

    # o(n) complexity, O(1) space
