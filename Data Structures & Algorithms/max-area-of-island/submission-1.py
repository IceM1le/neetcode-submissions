class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        max_size = 0
        rows, cols = len(grid), len(grid[0])
        def size_island(i, j):
            if grid[i][j] == 1:                
                count = 1
                grid[i][j] = 0
                if i + 1 < rows: count += size_island(i + 1, j)
                if i > 0: count += size_island(i - 1, j)
                if j + 1 < cols: count += size_island(i, j + 1)
                if j > 0: count += size_island(i, j - 1)
                return count
            return 0
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_size = max(size_island(i, j), max_size)
        return max_size