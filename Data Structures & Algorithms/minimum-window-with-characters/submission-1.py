class Solution:
    def minWindow(self, s: str, t: str) -> str:
        match = 0
        l = 0
        resLen = float("inf")
        tHash = defaultdict(int)
        sHash = defaultdict(int)
        for i in range(len(t)):
            tHash[t[i]] += 1
        for r in range(len(s)):
            sHash[s[r]] += 1
            if s[r] in tHash and sHash[s[r]] == tHash[s[r]]:
                match += 1


            while match == len(tHash):
                if resLen > r-l+1:
                    resLen = r-l+1
                    res = s[l:r+1]

                sHash[s[l]] -= 1
                if s[l] in tHash and sHash[s[l]] < tHash[s[l]]:
                    match -= 1
                l += 1
        

        if resLen == float('inf'):
            return ""

        return res