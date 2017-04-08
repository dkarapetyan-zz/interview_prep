# Write a function to find the longest common prefix string amongst an array
# of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        length = 0
        for i in range(len(strs[0])):
            for string in strs:
                if i > len(string) - 1:
                    return strs[0][:length]
                elif strs[0][i] != string[i]:
                    return strs[0][:length]
            length += 1
        return strs[0][:length]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["lipha", "lipaba", "lipmony"]))
