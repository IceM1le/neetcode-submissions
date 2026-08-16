from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: queue.append((i, j))
        while queue:            
            i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + di, j + dj
                if 0 <= row < m and 0 <= col < n and grid[row][col] == INF:
                    grid[row][col] = grid[i][j] + 1
                    queue.append((row, col))
