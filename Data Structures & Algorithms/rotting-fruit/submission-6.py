class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        from collections import deque
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        res = 0
        while queue:                        
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj 
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
            if len(queue) > 0:
                res += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return res