class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        def is_palindrome(i, j):
            while i < j:
                if not (s[i].isalnum()):
                    i += 1
                    continue
                if not (s[j].isalnum()):
                    j -= 1
                    continue
                
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l+1, r) or is_palindrome(l, r-1))
            l += 1
            r -= 1
        return True