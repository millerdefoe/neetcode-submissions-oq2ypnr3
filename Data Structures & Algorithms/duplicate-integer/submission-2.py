class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = defaultdict(int)
        for num in nums:
            h_map[num] += 1
            if h_map[num] > 1:
                return True

        return False