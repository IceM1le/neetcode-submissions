class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        from collections import deque
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        count = 0
        while queue:
            lvl = len(queue)
            for _ in range(lvl):
                i, j = queue.popleft()
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        queue.append((ni, nj))
                        grid[ni][nj] = 2            
            if len(queue):
                count += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return count