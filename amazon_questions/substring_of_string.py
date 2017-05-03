# Implement strStr().
#
#  strstr - locate a substring ( needle ) in a string ( haystack ).
# Try not to use standard library string functions for this question.
#
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
#  NOTE: Good clarification questions:
# What should be the return value if the needle is empty?
# What if both haystack and needle are empty?
# For the purpose of this problem, assume that the return value should be -1
# in both cases.

class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer

    # O(kn)
    def _strStr1(self, haystack, needle, i, j):
        if len(haystack[i:j + 1]) == 0 or len(needle) == 0:
            return -1

        output = self._strStr(haystack, needle, i + 1, j - 1)
        if output == -1:
            if haystack[i: i + len(needle)] == needle:
                return i
            elif haystack[j - len(needle) + 1: j + 1] == needle:
                return j - len(needle) + 1
        return output

    # O(kn), easier, gives first substr index

    def strStr(self, haystack, needle):
        if len(haystack) == 0 or len(needle) == 0 or len(needle) > len(
                haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    obj = Solution()
    haystack = 'bobexcattyexcelsior'
    needle = 'ex'
    print(obj.strStr(haystack, needle))
