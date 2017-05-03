# Given n non-negative integers a1, a2, ..., an, where each represents a
# point at coordinate (i, ai). n vertical lines are drawn such that the two
# endpoints of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container, such that the container
# contains the most water.
#
# Note: You may not slant the container and n is at least 2.

from itertools import product


class Solution(object):
    def maxArea_ineff(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_so_far = 0
        area = 0
        # max_indices = None

        for i, j in product(range(len(height)), range(len(height))):
            if height[i] == height[j]:
                area = (i - j) * height[i]
                if area >= max_so_far:
                    # max_indices = (i, j)
                    max_so_far = area
        return area

    # idea maximal subrectangle of a rectangle is the one where
    # min side is deleted--because we are decreasing width
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_so_far = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_so_far = max(area, max_so_far)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_so_far
