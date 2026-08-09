# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        dq = deque([root])
        while dq:
            node = dq.popleft()         
            if not node: continue
            node.left, node.right = node.right, node.left
            if node.left and node.right:
                dq.append(node.left)
                dq.append(node.right)
            else:
                if node.right:
                    dq.append(node.right)
                elif node.left:
                    dq.append(node.left)
        return root