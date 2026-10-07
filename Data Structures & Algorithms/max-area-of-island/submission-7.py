class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def max_island(i: int, j: int) -> None:
            self.count += 1
            grid[i][j] = 0
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    max_island(ni, nj)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.count = 0
                    max_island(i, j)
                    res = max(res, self.count)
        return res