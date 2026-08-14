class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        i = 1
        while i < n:
            while i < n and res[-1][1] >= intervals[i][0]:
                if res[-1][1] < intervals[i][1]: res[-1][1] = intervals[i][1]
                i += 1
            if i < n: 
                res.append(intervals[i])
                i += 1
        return res