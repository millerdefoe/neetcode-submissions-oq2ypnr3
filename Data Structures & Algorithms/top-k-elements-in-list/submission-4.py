import heapq

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        max_heap = []
        for key, value in counts.items():
            heapq.heappush(max_heap, (-value, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res