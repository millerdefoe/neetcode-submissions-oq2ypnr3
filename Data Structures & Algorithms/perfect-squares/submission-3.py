class Solution:
    def numSquares(self, n: int) -> int:
        

        def calculateRange(value:int)->int:
            value = value ** 0.5
            value = int(value)
            return value

        print(f'{calculateRange(13)=}')
        dp = [n] * (n + 1) #memoisation table
        
        dp[0] = 0

        for target in range(1, n + 1):
            perfectSquares = calculateRange(target)
            for s in range(1, perfectSquares+1):
                square = s ** 2
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        
        return dp[n]