# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        from collections import deque
        cur = deque()
        cur.append(root)
        while cur:            
            lvl = len(cur)
            cur_lvl = []
            for i in range(lvl):
                val_left = cur.popleft()
                if val_left.left: cur.append(val_left.left)
                if val_left.right: cur.append(val_left.right)
                cur_lvl.append(val_left.val)
            res.append(cur_lvl)
        return res