class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashm = defaultdict(int)
        l, n = 0, len(s)
        res = 0
        for r in range(n):
            hashm[s[r]] += 1
            while len(hashm) > k:
                hashm[s[l]] -= 1
                if hashm[s[l]] == 0:
                    del hashm[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res