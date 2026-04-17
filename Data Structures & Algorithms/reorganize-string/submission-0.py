class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = Counter(s)
        maxHeap = []
        for key, value in hashMap.items():
            heapq.heappush(maxHeap, (-value, key))
        
        prev = None
        res = ""
        while(maxHeap):
            count, char = heapq.heappop(maxHeap)
            res += char
            if prev:
                heapq.heappush(maxHeap, prev)
            prev = (count+1, char) if -(count) > 1 else None

        if len(res) == len(s):
            return res
        else:
            return ""       
