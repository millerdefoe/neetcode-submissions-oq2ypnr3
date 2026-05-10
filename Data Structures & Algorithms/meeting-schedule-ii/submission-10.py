"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []
        rooms = 0
        intervals.sort(key = lambda x:x.start)
        for interval in intervals:
            if not min_heap or min_heap[0] > interval.start:
                heapq.heappush(min_heap, interval.end)
                rooms += 1
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval.end)

        return rooms