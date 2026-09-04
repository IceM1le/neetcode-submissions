class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for s in stones: heapq.heappush(heap, -s)
        while len(heap) > 1:
            cur = heapq.heappop(heap) - heapq.heappop(heap)
            if cur: heapq.heappush(heap, cur)
        return -heapq.heappop(heap) if heap else 0