class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sort = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[sort]:
                sort += 1
                nums[sort] = nums[i]
        return sort + 1
                
