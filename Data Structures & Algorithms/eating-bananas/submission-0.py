
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound, upperBound = 1, max(piles)
        res = upperBound
        while lowerBound <= upperBound:
            mid = (lowerBound + upperBound) // 2
            time = 0
            for i in piles:
                time += math.ceil(float(i) / mid)
            if time <= h:
                res = mid
                upperBound = mid - 1
            else:
                lowerBound = mid + 1
                

        return res

