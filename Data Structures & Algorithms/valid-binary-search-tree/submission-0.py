# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(node, diapason):
            left, right = True, True
            if node.left: 
                left = diapason[0] < node.left.val < node.val and is_valid_bst(node.left, (diapason[0], node.val))
            if node.right: 
                right = node.val < node.right.val < diapason[1] and is_valid_bst(node.right, (node.val, diapason[1]))
            return left and right
        if not root: return False
        return is_valid_bst(root, (-float('inf'), float('inf')))