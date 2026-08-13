# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_sub_tree(node, sub_node):
            if not node and not sub_node: return True
            if not node or not sub_node: return False
            return node.val == sub_node.val and is_sub_tree(node.left, sub_node.left) and is_sub_tree(node.right, sub_node.right) 
        
        if not root or not subRoot: return False
        if is_sub_tree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)