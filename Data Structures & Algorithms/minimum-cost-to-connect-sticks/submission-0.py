class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = sticks
        heapq.heapify(minHeap)
        cost = 0
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            cost += x + y
            heapq.heappush(minHeap, x+y)
        
        return cost