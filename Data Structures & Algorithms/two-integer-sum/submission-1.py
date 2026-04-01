class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashm:
                return [hashm[diff], i]
            hashm[nums[i]] = i