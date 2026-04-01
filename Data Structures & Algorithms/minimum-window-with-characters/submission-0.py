class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tmap = defaultdict(int)
        smap = defaultdict(int)
        for i in range(len(t)):
            tmap[t[i]] += 1
        
        target = 0
        l = 0
        res = [-1,-1]
        length = 9999999999
        for r in range(len(s)):
            smap[s[r]] += 1
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                target += 1
            while target == len(tmap):
                if (length > r - l + 1):
                    res = [l,r]
                    length = r - l + 1
                smap[s[l]] -= 1
                
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    target -= 1
                l += 1
        print(res)
        return s[res[0]:res[1]+1] if length != 9999999999 else ""

            

