class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dpRow = [-prices[0], -float("inf"), 0]
        for i in range(1,len(prices)):
           dpCopy = dpRow.copy()
           dpRow[0] = max(dpCopy[0], dpCopy[2] - prices[i])
           dpRow[1] = dpCopy[0] + prices[i]
           dpRow[2] = max(dpCopy[2], dpCopy[1])
        return max(dpRow[1],dpRow[2])