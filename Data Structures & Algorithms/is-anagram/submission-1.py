class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        anagram2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            anagram[s[i]] = anagram.get(s[i], 0) + 1
            anagram2[t[i]] = anagram2.get(t[i], 0) + 1
        if anagram != anagram2:
            return False

        return True
        