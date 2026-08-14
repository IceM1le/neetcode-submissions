class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for p in points:            
            heapq.heappush(heap, ((-pow(p[0], 2) - pow(p[1], 2)), p))
            if len(heap) > k: heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res