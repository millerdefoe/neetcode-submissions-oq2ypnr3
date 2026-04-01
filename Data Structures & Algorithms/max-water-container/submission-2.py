class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        vmax = 0
        while start < end:
            volume = min(heights[start], heights[end]) * (end-start)
            if vmax < volume:
                vmax = volume
            if heights[start] < heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return vmax