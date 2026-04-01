class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashm = {} # distance, coordinate pair
        maxHeap = []
        
        for i in points:
            #calcuate dist
            dist = math.sqrt(i[0] ** 2 + i[1] ** 2)

            heapq.heappush(maxHeap, (-dist, i))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        res = []
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])
        return res

