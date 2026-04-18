class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        
        def dfs(start, segments):
            if start == len(s):
                res.append(" ".join(segments))
                return

            
            for i in range(start, len(s)):
                if s[start: i+1] in wordDict:
                    segments.append(s[start:i+1])
                    dfs(i+1, segments)
                    segments.pop()
            return 

        dfs(0, [])
        return res