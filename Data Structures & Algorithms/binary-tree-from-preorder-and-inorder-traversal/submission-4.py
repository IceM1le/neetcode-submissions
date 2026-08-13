# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}  # O(n) один раз

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])
            mid = idx_map[root.val]               # O(1) вместо O(n)
            left_size = mid - in_l

            root.left  = build(pre_l + 1, pre_l + left_size, in_l, mid - 1)
            root.right = build(pre_l + left_size + 1, pre_r, mid + 1, in_r)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)