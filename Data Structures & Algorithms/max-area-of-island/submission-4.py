class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_island = 0
        def count_island(i, j):
            if 0 <= i < n and 0 <= j < m:
                self.count += 1
                grid[i][j] = 0
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        count_island(ni, nj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.count = 0
                    count_island(i, j)
                    max_island = max(max_island, self.count)
        return max_island