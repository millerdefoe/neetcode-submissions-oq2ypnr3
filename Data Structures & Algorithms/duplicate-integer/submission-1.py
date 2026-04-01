class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] == 2:
                return True
        return False