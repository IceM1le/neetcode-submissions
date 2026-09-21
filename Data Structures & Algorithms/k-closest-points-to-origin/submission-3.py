class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0] ** 2 + p[1] ** 2, p))
        res = []
        for _ in range(k):
            cur = heapq.heappop(heap)
            res.append(cur[1])
        return res