class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = ""
        if len(word1) < len(word2):
            limit = len(word1)
            choose = 2
        else:
            limit = len(word2)
            choose = 1
        while i < limit:
            out += word1[i]
            out += word2[i]
            i += 1
        
        if choose == 1:
            out += word1[limit:]
        else:
            out += word2[limit:]
            
        
        return out