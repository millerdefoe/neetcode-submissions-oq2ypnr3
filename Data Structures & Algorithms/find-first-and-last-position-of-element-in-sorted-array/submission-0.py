class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1,-1]
        while l <= r:
            m = l + (r-l) // 2

            if m < len(nums) and nums[m] < target:
                l = m + 1
            elif m >= 0 and nums[m] > target:
                r = m - 1
            else:
                res = [m,m]
                while res[0] >= 1 and nums[res[0]-1] == target:
                    res[0] -= 1
                while res[1] < len(nums) -1 and nums[res[1]+1] == target:
                    res[1] += 1
                break

        return res