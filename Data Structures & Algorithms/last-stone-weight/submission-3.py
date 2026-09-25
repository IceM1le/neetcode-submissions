class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        while len(heap) > 1:
            val = heapq.heappop(heap) - heapq.heappop(heap)
            if val: heapq.heappush(heap, val)
        return 0 if not len(heap) else -heap[0]