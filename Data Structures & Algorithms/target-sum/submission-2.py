class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, rem):
            if i == len(nums) and rem == 0:
                    return 1
            if i == len(nums) and rem != 0:
                    return 0
            if (i, rem) in dp:
                    return dp[(i, rem)]
            dp[(i,rem)] = dfs(i+1, rem-nums[i]) + dfs(i+1, rem+nums[i])
            return dp[(i, rem)]

        return dfs(0, target)