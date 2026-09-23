# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def is_bal(node):
            if not node: return 0
            left = is_bal(node.left) 
            right = is_bal(node.right)
            if not abs(left - right) <= 1:
                self.is_balanced = False
            return 1 + max(left, right)
        is_bal(root)
        return self.is_balanced 