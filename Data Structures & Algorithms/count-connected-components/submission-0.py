class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        
        def all_neighbors(node):
            if node not in visited:
                visited.add(node)
                for neigbor in graph[node]:
                    all_neighbors(neigbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                all_neighbors(i)
        return count