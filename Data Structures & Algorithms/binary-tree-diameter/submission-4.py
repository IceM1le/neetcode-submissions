# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def depth(root: Optional[TreeNode]) -> int:
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            self.count = max(left + right, self.count)
            return max(left, right) + 1
        depth(root)
        return self.count