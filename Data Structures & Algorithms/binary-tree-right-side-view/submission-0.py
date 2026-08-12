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
        dq = deque()
        dq.append(root)
        res = []        
        while dq:
            lvl = len(dq)
            for i in range(lvl):                
                left_val = dq.popleft()            
                if i + 1 == lvl: res.append(left_val.val)
                if left_val.left: dq.append(left_val.left)
                if left_val.right: dq.append(left_val.right)
        return res