class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bSearch(nums, target, True)
        right = self.bSearch(nums, target, False)
        res = [left, right]
        return res
        
    def bSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = l + (r-l) // 2

            if m < len(nums) and nums[m] < target:
                l = m + 1
            elif m >= 0 and nums[m] > target:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
                
