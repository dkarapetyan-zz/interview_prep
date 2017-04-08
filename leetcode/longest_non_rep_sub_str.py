# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    @staticmethod
    # order o(n) algorithm. Hashtable holds sentinel
    def length_longest_substring(s):
        n = len(s)
        ans = 0
        start = end = 0
        table = {}

        while start < n and end < n:
            if table.get(s[end], None) is None:
                table[s[end]] = -1
                end += 1
            else:
                ans = max(ans, end - start)
                table.pop(s[start], None)
                start += 1
        return max(ans, end - start)

    # o(n) algorithm. Hashtable holds more info than just sentinel :)
    def length_ls(self, s):
        ans = start = 0
        table = {}

        for j, char in enumerate(s):
            if not table.get(char, None):
                table[char] = 1  # character has occurred once; keep track
            else:
                ans = max(ans, j - start)
                start = j + 1
                table = {}  # flush table and start again
        return max(ans, len(s) - start)


if __name__ == '__main__':
    obj = Solution()
    print(obj.length_ls("qwnfenpglqdq"))
