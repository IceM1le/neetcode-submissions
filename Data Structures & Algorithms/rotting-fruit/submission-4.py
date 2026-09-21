class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        from collections import deque
        n, m = len(grid), len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: queue.append((i, j))
        counter = 0
        while queue:
            minute = len(queue)            
            for _ in range(minute):
                i, j = queue.popleft()
                for ni, nj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    di, dj = i + ni, j + nj
                    if 0 <= di < n and 0 <= dj < m and grid[di][dj] == 1:
                        queue.append((di, dj))
                        grid[di][dj] = 2 
            if len(queue): counter += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: return -1
        return counter