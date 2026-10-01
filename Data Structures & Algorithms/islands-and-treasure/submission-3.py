class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return
        WATER, CHEST, INF = -1, 0, 2147483647
        n, m = len(grid), len(grid[0])
        from collections import deque
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == CHEST:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                    queue.append((ni, nj))
                    grid[ni][nj] = grid[i][j] + 1
