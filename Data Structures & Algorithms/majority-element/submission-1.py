class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_val = len(nums) // 2
        hashm = {}
        for i, val in enumerate(nums):
            hashm[val] = hashm.get(val, 0) + 1
            if hashm[val] > maj_val:
                return val
        
        