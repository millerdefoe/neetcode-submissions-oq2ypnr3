class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target_value = sum(nums) // k

        used = [False] * len(nums)

        def dfs(k, sub_sum):
            if k == 0:
                return True
            if sub_sum == target_value:
                return dfs(k-1, 0)
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                if sub_sum + num > target_value:
                    continue
                used[i] = True
                if dfs(k, sub_sum + num):
                    return True 
                used[i] = False

                if sub_sum == 0:
                    return False

            return False
        
        return dfs(k, 0)