class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = defaultdict(int)
        prefix = 0
        prefix_hash[0] = 1
        res = 0
        for num in nums:
            prefix += num
            
            if prefix-k in prefix_hash:
                res += prefix_hash[prefix-k]

            prefix_hash[prefix] += 1

        return res