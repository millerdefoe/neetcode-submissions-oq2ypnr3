class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        i, j = 0, len(s)-1
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