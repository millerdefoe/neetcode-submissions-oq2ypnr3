class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol = 0
        maxh = {}
        while l < r:
            space = r - l
            calculated = space * min(heights[r], heights[l])
            maxh[calculated] = (l, r)
            if (heights[r] >= heights[l]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
        print(maxh)
        return max(maxh)