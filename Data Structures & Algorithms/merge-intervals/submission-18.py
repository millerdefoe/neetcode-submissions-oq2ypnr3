class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:        # overlaps with last merged
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval) 
        
        return res

            
            
