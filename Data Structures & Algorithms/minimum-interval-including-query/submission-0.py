class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

            