class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        NOT_VISITED, VISITED, DONE = 0, 1, 2
        graph = defaultdict(list)

        for n, c in prerequisites:
            graph[c].append(n)
        
        state = [NOT_VISITED] * numCourses

        def has_cycle(node):
            if state[node] == VISITED: return True
            if state[node] == DONE: return False

            state[node] = VISITED
            for n in graph[node]:
                if has_cycle(n): return True
            state[node] = DONE
            return False
        
        for i in range(numCourses):
            if state[i] == NOT_VISITED and has_cycle(i): return False
        return True
