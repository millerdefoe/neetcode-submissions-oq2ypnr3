class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for t, target in enumerate(nums):
            if t > 0 and nums[t] == nums[t-1]:
                continue
            l = t + 1
            r = len(nums) - 1
            while l < r:
                cur_total = nums[l] + nums[r] + target
                if cur_total > 0:
                    r -= 1
                elif cur_total < 0:
                    l += 1
                else:
                    res.append([nums[r], nums[l], target])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


            