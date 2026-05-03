import heapq
from collections import defaultdict

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        #capital_to_profit dict, key: value captial: profit maxHeapbucket
        minCapital = [(c, p)for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        
        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxHeap, -p)
        
            if not maxHeap:
                break
        
            w += -heapq.heappop(maxHeap)

        return w