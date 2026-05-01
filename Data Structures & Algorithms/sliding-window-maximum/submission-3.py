from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #calling max on an element
        queue = deque()

        #monotonic decreasing queue, so the front of q will hold the biggest element, and since its monotonic when we insert a bigger element we pop til nothing is smaller

        l, r = 0, 0
        res = []

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        
        return res