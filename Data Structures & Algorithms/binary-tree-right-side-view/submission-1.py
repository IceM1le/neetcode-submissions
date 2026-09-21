# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            lvl = len(queue)
            for i in range(lvl):
                cur = queue.popleft()
                if i + 1 == lvl: res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return res