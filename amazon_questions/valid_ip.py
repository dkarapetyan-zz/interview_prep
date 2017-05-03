# Valid Ip AddressesBookmark Suggest Edit
# Given a string containing only digits, restore it by returning all possible
#  valid IP address combinations.
#
# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are
# numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
#
# Example:
#
# Given "25525511135",  return ["255.255.11.135", "255.255.111.35"].
# (Make sure the returned strings are sorted in order)

class Solution:
    # @param A : string
    # @return a list of strings
    def _valid_ip(self, index, dots, A):
        if len(A) == 0 or index > len(A) or dots < 0:
            return []

        final = []
        for i in range(1, 4):
            output = self._valid_ip(index + i, dots - 1, A)
            if A[:i] <= '255':
                if dots == 0:
                    final.append(["." + A[:i]])
                else:
                    final.append([A[:i] + "." + item for item in output])
        return final

    def restoreIpAddresses(self, A):
        return self._valid_ip(0, 3, A)


if __name__ == '__main__':
    obj = Solution()
    print(obj.restoreIpAddresses("25525511135"))
