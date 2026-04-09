class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        delete = 0
        for i in range(1, len(intervals)):
            if prev[1] <= intervals[i][0]:
                prev = intervals[i]
            else:
                delete += 1
        return delete