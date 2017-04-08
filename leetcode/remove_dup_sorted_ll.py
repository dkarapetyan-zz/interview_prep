# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        p = head
        f = head.next
        while f is not None:
            if f.val != p.val:
                p.next = f
                p = f
                f = f.next
            else:
                p.next = f.next
                f = f.next

        return head
