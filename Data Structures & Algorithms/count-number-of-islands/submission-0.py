class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid[0]), len(grid)
        def find_island(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if j + 1 < n: find_island(i, j + 1)
                if j > 0: find_island(i, j - 1)
                if i + 1 < m: find_island(i + 1, j)
                if i > 0: find_island(i - 1, j)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    find_island(i, j)
        return count