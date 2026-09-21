# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            cur_res = []
            for _ in range(n):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                cur_res.append(cur.val)
            res.append(cur_res)
        return res