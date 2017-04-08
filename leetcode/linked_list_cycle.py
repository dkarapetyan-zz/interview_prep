# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # using extra memory
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        table = {}
        p = head
        while p is not None:
            if table.get(hash(p), None) is not None:
                return True
            else:
                table[hash(p)] = 1
                p = p.next
        return False

    # no extra memory

    def hasCycle(self, head):

        if head is None:
            return False

        p = head
        q = head.next

        while q is not None and q.next is not None:
            if p == q:
                return True
            else:
                p = p.next
                q = q.next.next
        return False
