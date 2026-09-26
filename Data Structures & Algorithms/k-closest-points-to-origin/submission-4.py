class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []        
        for p in points:
            heapq.heappush(heap, (-p[0] ** 2 - p[1] ** 2, p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [res[1] for res in heap]