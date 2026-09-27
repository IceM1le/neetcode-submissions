# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, diap):
            left, right = True, True
            if node.left:
                left = diap[0] < node.left.val < node.val and is_valid(node.left, (diap[0], node.val))
            if node.right:
                right = diap[1] > node.right.val > node.val and is_valid(node.right, (node.val, diap[1]))
            return left and right
        return is_valid(root, (-float('inf'), float('inf')))