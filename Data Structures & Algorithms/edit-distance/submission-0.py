
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)
        dp = [[-1] * COLS for _ in range(ROWS)]
        def dfs(r, c):
            if r == ROWS:
                return COLS - c #Append remaining characters in target word2
            if c == COLS:
                return ROWS - r #we are done matching need to delete excess
            if dp[r][c] != -1:
                return dp[r][c]
            if word1[r] == word2[c]:
                dp[r][c] = dfs(r+1,c+1)
            else:
                dp[r][c] = 1 + min(dfs(r+1,c), dfs(r,c+1), dfs(r+1,c+1))
            return dp[r][c]
        return dfs(0,0)
    
            
            