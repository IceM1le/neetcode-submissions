# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def depth(node: Optional[TreeNode]) -> int:
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            if not abs(left - right) <= 1: self.balanced = False
            return 1 + max(left, right)
        depth(root)
        return self.balanced