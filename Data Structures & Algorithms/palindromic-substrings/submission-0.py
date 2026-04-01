class Solution:
    def countSubstrings(self, s: str) -> int:
        resTable = [[False] * len(s) for _ in range(len(s))]
        # resTable[i:j] = True then i to j is a palindrome
        n = len(s)
        res = []
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or resTable[i+1][j-1]):
                    resTable[i][j] = True
                    res.append(s[i:j+1])
        return len(res)