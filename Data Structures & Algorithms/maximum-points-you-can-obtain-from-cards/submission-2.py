class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k

        if len(cardPoints) == k:
            return sum(cardPoints)
         
        res = resTemp = sum(cardPoints[l:r])
        while r < len(cardPoints):
            resTemp -= cardPoints[l]
            l += 1
            resTemp += cardPoints[r]
            r += 1
            
            res = min(res, resTemp)
        
        return sum(cardPoints) - res
