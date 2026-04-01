class Solution:
    def trap(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1
        maxLeft = height[i]
        maxRight = height[j]
        volume = 0
        while i < j:
            if maxLeft > maxRight:
                
                j -= 1
                if height[j] > maxRight:
                    maxRight = height[j]
                volume += maxRight - height[j]
            else:
                
                i += 1
                if height[i] > maxLeft:
                    maxLeft = height[i]
                volume += maxLeft - height[i]

        return volume