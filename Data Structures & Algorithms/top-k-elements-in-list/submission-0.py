class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {} #VALUE:COUNT
        output = [0] * k
        for n in nums:
            hmap[n] = hmap.get(n,0) + 1
        for i in range(k):
            maxi = max(hmap, key=hmap.get)
            output[i] = maxi
            hmap[maxi] = 0
        return output
