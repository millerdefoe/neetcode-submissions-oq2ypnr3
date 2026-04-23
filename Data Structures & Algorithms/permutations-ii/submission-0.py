class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(array):
            if len(array) >= len(nums):
                res.append(array[:])
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    array.append(nums[i])
                    used[i] = True
                    dfs(array)
                    array.pop()
                    used[i] = False
        
        nums.sort()
        dfs([])
        return res