# Given a linked list, remove the nth node from the end of list and return
# its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next

        if length - n == 0:
            head = head.next
            return head
        else:
            prev_node = head
            for i in range(length - n - 1):  # iterate up to one node before
                # node to delete
                prev_node = prev_node.next
            prev_node.next = prev_node.next.next
            return head
