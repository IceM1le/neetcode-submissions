# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            if pre_r < pre_l: return 
            root = TreeNode(preorder[pre_l])
            mid = idx_map[root.val]
            size_left = mid - in_l

            root.left = build(pre_l + 1, pre_l + size_left, in_l, mid - 1)
            root.right = build(pre_l + size_left + 1, pre_r, mid + 1, in_r)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)