class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        def dfs(r, c, prev):
            if r == ROWS or c == COLS or r < 0 or c < 0:
                return 0
            if matrix[r][c] <= prev:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            prev = matrix[r][c]
            dp[r][c] = 1 + max(dfs(r+1,c, prev), dfs(r-1,c, prev), dfs(r,c+1, prev), dfs(r,c-1, prev))
            return dp[r][c]
        maxLen = 0
        for i in range(ROWS):
            for j in range(COLS):
                tempLen = dfs(i,j,-1)
                maxLen = max(maxLen, tempLen)
              
        return maxLen
