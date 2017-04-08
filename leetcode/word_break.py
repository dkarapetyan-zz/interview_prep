class Solution(object):
    # too slow for leetcode (time limit exceeded)
    def _wordBreak2(self, s, the_dict):
        # base case
        if len(s) == 1:
            if the_dict.get(s, None) is None:
                return False
            else:
                return True

        # inductive step
        if the_dict.get(s) is not None:
            return True

        for i in range(1, len(s)):
            if the_dict.get(s[:i], None) is not None and \
                            self.wordBreak(s[i:], the_dict) is True:
                return True

        return False

    # with memoization
    # time limit exceeded--still not fast enough
    # leetcode hates recursion--prefers iterative approach, which is indeed
    # a bit faster, but not as intuitive
    def _wordBreak(self, s, the_dict):
        # base case
        if len(s) == 1:
            if the_dict.get(s, None) is None:
                return False
            else:
                return True

        # inductive step
        if the_dict.get(s, None) is not None:
            return True

        for i in range(1, len(s)):
            if the_dict.get(s[i:], None) is None:
                the_dict[s[i:]] = self.wordBreak(s[i:], the_dict)
            if the_dict.get(s[:i], None) is True and the_dict[s[i:]] is True:
                the_dict[s] = True
                return True
            else:
                the_dict[s] = False

        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        the_dict = {item: True for item in wordDict}
        the_dict[''] = True
        return self._wordBreak(s, the_dict)


if __name__ == '__main__':
    s = "aaaaaaa"
    wordDict = ["aaaa", "aa"]

    obj = Solution()
    print(obj.wordBreak(s, wordDict))
