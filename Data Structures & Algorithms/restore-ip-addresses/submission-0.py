class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(start, parts):
            if len(parts) == 4 and start == len(s):
                res.append(".".join(parts))
                return

            if len(parts) == 4:
                return
            
            if start >= len(s):
                return

            for length in range(1, 4):
                segment = s[start: start + length]
                if len(segment) > 1 and segment[0] == '0':
                    break
                if int(segment) > 255:
                    break
                dfs(start + length, parts + [segment])
        
        dfs(0, [])
        return res