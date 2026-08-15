"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        count = 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        for i in range(len(intervals)):
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            count = max(count, len(heap))
        return count