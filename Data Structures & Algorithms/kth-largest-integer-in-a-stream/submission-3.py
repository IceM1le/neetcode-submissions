import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i, num in enumerate(nums):
            heapq.heappush(self.heap, num)
            if i >= k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) == self.k + 1: heapq.heappop(self.heap)
        return self.heap[0]