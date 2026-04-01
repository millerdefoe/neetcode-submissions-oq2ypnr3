class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curRow = [0] * n
        nextRow = [1] * n
        
        curRow[n-1] = 1
        for _ in range(m-1):
            curCopy = curRow.copy()
            for i in range(n-2, -1, -1):
                curRow[i] = curRow[i+1] + nextRow[i]
            
            nextRow = curRow
            curRow = curCopy
            
        
        return nextRow[0]
