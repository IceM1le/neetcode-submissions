class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        n, m = len(grid[0]), len(grid)
        count = 0
        def clear_island(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i + 1 < m: clear_island(i + 1, j)
                if j + 1 < n: clear_island(i, j + 1)
                if i - 1 >= 0: clear_island(i - 1, j)
                if j - 1 >= 0: clear_island(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    clear_island(i, j)
        return count