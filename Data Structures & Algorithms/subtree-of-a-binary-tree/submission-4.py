# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_sub(node, subNode):            
            if not node and not subNode: return True
            if not node or not subNode: return False
            return node.val == subNode.val and is_sub(node.left, subNode.left) and is_sub(node.right, subNode.right)
        if not root or not subRoot: return False
        if is_sub(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)