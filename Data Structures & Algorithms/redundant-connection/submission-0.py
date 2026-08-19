class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        def has_cycle(node, parent, visited):
            if node not in visited:
                visited.add(node)
                for n in graph[node]:
                    if n == parent: continue
                    if n in visited: 
                        res.append([n, node])
                        return True
                    if has_cycle(n, node, visited): return True
            return False
        
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            has_cycle(a, b, set())

        return res[0]