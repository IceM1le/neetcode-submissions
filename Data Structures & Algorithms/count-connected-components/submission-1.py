class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def has_cycle(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent or neighbor in visited: 
                    continue
                else: 
                    has_cycle(neighbor, node)
        res = 0
        for node in range(n):
            if node not in visited:
                has_cycle(node, -1)
                res += 1
        return res