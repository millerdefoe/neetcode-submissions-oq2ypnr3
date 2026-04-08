class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:      # no overlap
                res.append(newInterval)
                newInterval = intervals[i]
            else:                                      # overlap → merge
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)   # always commit the last one
        return res