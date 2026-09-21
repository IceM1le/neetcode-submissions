class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n, m = len(grid[0]), len(grid)
        max_size_island = 0
        def max_size(i, j):
            if grid[i][j] == 1:
                summa = 1
                grid[i][j] = 0
                if i + 1 < m: summa += max_size(i + 1, j)
                if j + 1 < n: summa += max_size(i, j + 1)
                if i - 1 >= 0: summa += max_size(i - 1, j)
                if j - 1 >= 0: summa += max_size(i, j - 1)
                return summa                   
            else: return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_size_island = max(max_size(i, j), max_size_island)
        return max_size_island