class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def has_cycle(node, parent, visited):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor == parent: 
                        continue                    
                    if neighbor in visited or has_cycle(neighbor, node, visited):
                        return True
            return False
        
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            if has_cycle(a, b, set()):
                return [a, b]
        return []