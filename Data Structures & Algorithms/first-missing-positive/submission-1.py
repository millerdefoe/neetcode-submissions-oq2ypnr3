class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])

            target = abs(nums[i]) - 1
            if 1 <= val <= len(nums):
                if nums[target] == 0:
                    nums[target] = -(len(nums) + 1)
                elif nums[target] > 0:
                    nums[target] = -nums[target]
        
        for i in range(len(nums)):
            value = i + 1
            if nums[i] >= 0:
                return value   
        return len(nums) + 1        