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
        dq = deque()
        dq.append(root)
        while dq:                        
            level = len(dq)
            res_lvl = []
            for i in range(level):
                lvl = dq.popleft()
                if lvl.left: dq.append(lvl.left)
                if lvl.right: dq.append(lvl.right)
                res_lvl.append(lvl.val)
            res.append(res_lvl)
        return res
