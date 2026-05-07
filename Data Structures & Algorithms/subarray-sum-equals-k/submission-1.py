class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = defaultdict(int)
        count[0] = 1

        for num in nums:
            prefix += num
            res += count[prefix - k]
            count[prefix] += 1
        
        return res