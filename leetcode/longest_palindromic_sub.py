# Given a string s, find the longest palindromic substring in s. You may
# assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

class Solution(object):
    def _expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        right -= 1
        left += 1
        return left, right, right - left + 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_tuple = (0, 0)
        length = -1

        for i in range(len(s)):
            x = self._expand_around_center(s, i, i + 1)
            y = self._expand_around_center(s, i, i)
            z = max(x, y, key=lambda tu: tu[2])
            if z[2] > length:
                length = z[2]
                max_tuple = (z[0], z[1])
        return s[max_tuple[0]: max_tuple[1] + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome('bobhelehlkjwer'))
