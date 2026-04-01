class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {} #VALUE:COUNT
        freq = [[] for i in range(len(nums)+1)]
        res = []
        output = [0] * k
        for n in nums:
            hmap[n] = hmap.get(n,0) + 1
        for n, v in hmap.items():
            freq[v].append(n)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res