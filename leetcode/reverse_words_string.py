# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_of_words = s.split(" ")
        lw_no_dup = [item for item in list_of_words if item != '']
        lw_reversed = list(reversed(lw_no_dup))
        if set(lw_reversed) == {""} or len(lw_reversed) == 0:
            return ""
        return " ".join(lw_reversed)


if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseWords("a"))
