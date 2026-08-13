# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.counter = 0
        def is_good(node, max_val):
            if not node: return
            if node.val >= max_val: 
                self.counter += 1
                max_val = node.val
            is_good(node.left, max_val)
            is_good(node.right, max_val)
        is_good(root, root.val)
        return self.counter