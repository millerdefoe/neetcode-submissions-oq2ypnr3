class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        minLen = 99999
        l, r = 0, 0
        
        while r < len(nums):
            print(curSum, target, l ,r)
            
            if curSum < target:
                curSum += nums[r]
                r += 1
            while curSum >= target:
                minLen = min(minLen, r - l)
                curSum -= nums[l]
                l += 1
                
                
        if minLen == 99999:
            return 0
        return minLen
