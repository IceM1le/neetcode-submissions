from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for i in range(rows): 
            for j in range(cols):
                if grid[i][j] == 0: queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))