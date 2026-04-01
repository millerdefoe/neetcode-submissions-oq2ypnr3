class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleaned += s[i]
        cleaned = cleaned.lower()
        end = len(cleaned) - 1
        if cleaned == "": return True
        for i in range(len(s) // 2):
            if cleaned[i] != cleaned[end]:
                return False
            end -= 1
        return True