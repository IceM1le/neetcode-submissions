"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        old_to_new = {}
        from collections import deque
        old_to_new[node] = Node(node.val)
        queue = deque([node])
        while queue:
            new_node = queue.popleft()
            for n in new_node.neighbors:
                if n not in old_to_new:
                    old_to_new[n] = Node(n.val)
                    queue.append(n)
                old_to_new[new_node].neighbors.append(old_to_new[n])
        return old_to_new[node]