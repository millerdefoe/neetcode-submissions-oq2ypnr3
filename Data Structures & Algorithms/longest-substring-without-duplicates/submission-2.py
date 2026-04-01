class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        maxcount = 0
        l,r = 0, 0
        count = 0
        while r < len(s):
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
                count -= 1
            else:
                substring.add(s[r])
                r += 1
                count += 1
                maxcount = max(maxcount, count)
        return maxcount