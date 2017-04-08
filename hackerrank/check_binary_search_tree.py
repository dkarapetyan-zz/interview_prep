""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check_binary_search_tree_(root):
    if root.left is None and root.right is None:
        return True

    if root.left is not None:
        if root.left.data >= root.data:
            return False
        if root.left.right is not None:
            if root.left.right.data >= root.data:
                return False
    if root.right is not None:
        if root.right.data <= root.data:
            return False
        if root.right.left is not None:
            if root.right.left.data <= root.data:
                return False

    if root.left is not None and root.right is not None:
        if root.left.right is not None and root.right.left is not None:
            if root.left.right.data == root.right.left.data:
                return False

    bool_left = check_binary_search_tree_(root.left)
    bool_right = check_binary_search_tree_(root.right)

    return bool_left & bool_right
