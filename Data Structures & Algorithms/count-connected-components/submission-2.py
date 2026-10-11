class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def has_cycle(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited: 
                    has_cycle(neighbor, node)                    
        
        res = 0
        for i in range(n):
            if i not in visited:
                has_cycle(i, -1)
                res += 1
        return res