class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m, n = len(heights), len(heights[0])
                
        def add_to_set(i, j, set_ocean):
            if (i, j) not in set_ocean:
                set_ocean.add((i, j))
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and heights[i][j] <= heights[ni][nj]:
                        add_to_set(ni, nj, set_ocean)
        
        atlantic, pacific = set(), set()
        for i in range(n):
            add_to_set(0, i, pacific)
            add_to_set(m-1, i, atlantic)
        for i in range(m):
            add_to_set(i, 0, pacific)
            add_to_set(i, n-1, atlantic)            
        return [list(st) for st in atlantic & pacific]