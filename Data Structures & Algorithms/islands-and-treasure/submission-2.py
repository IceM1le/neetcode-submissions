class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return 
        from collections import deque
        INF = 2147483647
        queue = deque()
        m, n = len(grid[0]), len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for ni, nj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                di, dj = i + ni, j + nj
                if 0 <= di < n and 0 <= dj < m and grid[di][dj] == INF:
                    grid[di][dj] = grid[i][j] + 1
                    queue.append((di, dj))