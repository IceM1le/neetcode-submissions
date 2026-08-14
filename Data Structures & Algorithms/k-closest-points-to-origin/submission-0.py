class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math, heapq
        heap = []
        for p in points:
            heapq.heappush(heap, (math.sqrt(pow(p[0], 2) + pow(p[1], 2)), p))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res