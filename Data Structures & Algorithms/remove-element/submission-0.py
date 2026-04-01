class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i, value in enumerate(nums):
            if value == val:
                continue
            else:
                nums[i] = nums[j]
                nums[j] = value
                j += 1
                
        return j