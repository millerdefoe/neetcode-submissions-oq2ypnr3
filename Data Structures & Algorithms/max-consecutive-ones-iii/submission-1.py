class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #sliding window size return. max would be len(nums). minimum k
        l, r = 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max(res, r - l + 1)

            r += 1

        return res