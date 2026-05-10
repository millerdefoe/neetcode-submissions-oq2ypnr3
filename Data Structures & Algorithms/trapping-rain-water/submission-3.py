class Solution:
    def trap(self, height: List[int]) -> int:
        left_stack = [0] #are monotonically increasing
        right_stack = [0]

        for i in range(len(height)-1):
            val = left_stack[-1]
            if val < height[i]:
                left_stack.append(height[i])
            else:
                left_stack.append(val)
        
        for i in range(len(height)-1, 0, -1):
            val = right_stack[-1]
            if val < height[i]:
                right_stack.append(height[i])
            else:
                right_stack.append(val)
        res = 0
        for i, water in enumerate(height):
            temp = min(right_stack[~i], left_stack[i]) - water
            if temp >= 0:
                res += temp
        return res

