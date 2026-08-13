# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def depth(node):
            if not node: return 0
            left = max(depth(node.left), 0)
            right = max(0, depth(node.right))
            self.max_sum = max(left + right + node.val, self.max_sum)
            return max(left, right) + node.val
        depth(root)
        return self.max_sum 