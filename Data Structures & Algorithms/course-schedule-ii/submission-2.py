class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        UNVISITED, VISITED, DONE = 0, 1, 2
        graph = defaultdict(list)
        for n, c in prerequisites: graph[c].append(n)
        state = [UNVISITED] * numCourses
        res = []

        def has_cycle(node):
            if state[node] == VISITED: return True
            if state[node] == DONE: return False
            state[node] = VISITED
            for n in graph[node]:
                if has_cycle(n): return True
            state[node] = DONE
            res.append(node)
            return False

        for i in range(numCourses):
            if state[i] == UNVISITED and has_cycle(i): return []
        return res[::-1]