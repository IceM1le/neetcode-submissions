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
            for n in graph[node]:
                if n == parent: continue
                if n in visited: return True
                if has_cycle(n, node): return True
            return False
        if has_cycle(0, -1): return False
        return len(visited) == n