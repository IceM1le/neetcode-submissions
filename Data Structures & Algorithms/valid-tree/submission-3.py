class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        
        def has_cycle(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if neighbor in visited or has_cycle(neighbor, node):
                    return True
            return False
        
        if has_cycle(0, -1):
            return False
        return len(visited) == n