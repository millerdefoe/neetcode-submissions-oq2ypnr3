class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        l, r = 0,0
        size = 0
        for r in range(len(nums)):
            k -= 1 if nums[r] == 0 else 0
            while k < 0:
                k += (1 if nums[l] == 0 else 0)
                l += 1
            size = max(size, r - l + 1)
            
        return size
                