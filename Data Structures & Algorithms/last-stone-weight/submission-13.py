class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap, -(x-y))
            elif y > x:
                heapq.heappush(maxHeap, -(y-x))

        
        if maxHeap:
            return -maxHeap[0]
        return 0
            