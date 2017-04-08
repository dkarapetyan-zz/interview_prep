# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

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
        len_l1 = len_l2 = 0
        p, q = l1, l2

        while p is not None:
            len_l1 += 1
            p = p.next

        while q is not None:
            len_l2 += 1
            q = q.next

        final = 0
        p, q = l1, l2

        i = 0
        while i < len_l1:
            final += 10 ** i * p.val
            p = p.next
            i += 1

        j = 0
        while j < len_l2:
            final += 10 ** j * q.val
            q = q.next
            j += 1

        head = ListNode(None)
        p = head
        while final:
            p.val = final % 10
            if final / 10 == 0:
                break
            else:
                final /= 10
                p.next = ListNode(None)
                p = p.next
        return head
