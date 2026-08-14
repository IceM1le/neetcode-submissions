class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for stone in stones: heapq.heappush(heap, -stone)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -abs(first - second))
        return -heap[0] if len(heap) else 0