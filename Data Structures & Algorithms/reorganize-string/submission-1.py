class Solution:
    def reorganizeString(self, s: str) -> str:
        hMap = defaultdict(int)
        for c in s:
            hMap[c] += 1
        
        maxHeap = []
        for key in hMap.keys():
            heapq.heappush(maxHeap, [-hMap[key], key])
        holder = None
        res = []
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            count = -count
            res.append(letter)
            count -= 1
            if holder:
                heapq.heappush(maxHeap, holder)
                holder = None
            if count > 0:
                holder = [-count, letter]
            
        if holder:
            return ""
        else:
            return "".join(res)
