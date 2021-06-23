""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    return checkBST_main(root)


def checkBST_main(tree, min_val=float('-inf'), max_val=float('inf')):
    # Reached leaf if not tree
    if not tree:
        return True
    # Check if current node satisfies the constraint
    elif not min_val <= tree.data <= max_val:
        return False
    # Recursively check left subtree and right subtree
    return (checkBST_main(tree.left, min_val, tree.data) and checkBST_main(tree.right, tree.data, max_val))
