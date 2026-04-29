class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, solution, remainder):
            if remainder < 0:
                return
            
            if remainder == 0:
                res.append(solution.copy())
                return
            
            solution.append(nums[i])
            dfs(i, solution, remainder - nums[i])
            solution.pop()

            if i+1 < len(nums):
                dfs(i+1, solution, remainder)
            
            return

        

        dfs(0, [], target)
        print(res)
        return res