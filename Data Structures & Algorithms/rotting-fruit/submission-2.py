from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        if not grid: return -1
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: queue.append((i, j))
        minute = 0
        while queue:                        
            rotting = len(queue)
            for _ in range(rotting):
                i, j = queue.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
            if len(queue): minute += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return minute