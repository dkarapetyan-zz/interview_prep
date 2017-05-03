# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# Example :
#
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def _max_ending_at_node(self, the_node):
        if the_node is None:
            return 0
        else:
            l = self._max_ending_at_node(
                the_node.left)
            r = self._max_ending_at_node(
                the_node.right)
            max_uni_dir = max(the_node.val, the_node.val + max(l, r))
            max_so_far = max(self.max_so_far, max_uni_dir, l + r + the_node.val)
            # min path sum
            # with this node assumed to be root. One such node will indeed
            # be the head of the tree with the largest path
            self.max_so_far = max_so_far
            return max_uni_dir

    def maxPathSum(self, A):
        self.max_so_far = -float('inf')
        self._max_ending_at_node(A)
        return self.max_so_far
