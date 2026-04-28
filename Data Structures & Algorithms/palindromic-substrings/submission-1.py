class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for center in range((len(s) * 2) - 1):
            if center % 2:
                left = (center - 1) // 2
                right = left + 1
            
            else:
                left = right = center // 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res
