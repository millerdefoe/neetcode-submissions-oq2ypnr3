class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        count = 0
        counthigh = 0
        for i in res:
            if ((i-1) not in res):
                count = 0
                while (i + count) in res:
                    count += 1
                counthigh = max(count, counthigh)
        return counthigh