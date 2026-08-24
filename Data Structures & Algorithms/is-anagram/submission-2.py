class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        h_s, h_t = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            h_s[s[i]] += 1
            h_t[t[i]] += 1
        
        return h_s == h_t