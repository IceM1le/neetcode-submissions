class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        def add_in_ocean(i: int, j: int, ocean: set) -> None:
            ocean.add((i, j))
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in ocean and heights[ni][nj] >= heights[i][j]:
                    add_in_ocean(ni, nj, ocean)
        
        pacific, atlantic = set(), set()
        for i in range(n):
            add_in_ocean(i, 0, pacific)
            add_in_ocean(i, m - 1, atlantic)
        for j in range(m):
            add_in_ocean(0, j, pacific)
            add_in_ocean(n - 1, j, atlantic)
        return [list(tpl) for tpl in pacific & atlantic]