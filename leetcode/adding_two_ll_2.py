# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1, list_2 = [], []
        while l1 is not None:
            list_1.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            list_2.append(str(l2.val))
            l2 = l2.next

        final_num_temp = int("".join(list_1)) + int("".join(list_2))
        final_num_list = list(reversed(list(str(final_num_temp))))
        length = len(final_num_list)
        final_num = int("".join(final_num_list))

        head = ListNode(None)
        p = head

        for i in range(length):
            p.val = final_num % 10
            if i != length - 1:
                p.next = ListNode(None)
                p = p.next
            final_num /= 10
        return head
