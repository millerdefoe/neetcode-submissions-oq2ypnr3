"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        if not len(intervals):
            return 0
        minHeap = [intervals[0].end]
        for i in range(1,len(intervals)):
            if intervals[i].start < minHeap[0]:
                heapq.heappush(minHeap, intervals[i].end)
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, intervals[i].end)
        return len(minHeap)
