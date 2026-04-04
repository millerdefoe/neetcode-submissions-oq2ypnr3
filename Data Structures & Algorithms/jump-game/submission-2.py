class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        maxReach = nums[i]
        while i != maxReach and i != (len(nums)-1):
            i += 1
            maxReach = max(nums[i] + i, maxReach)
            

        
        if maxReach >= (len(nums) - 1):
            return True
        return False
        