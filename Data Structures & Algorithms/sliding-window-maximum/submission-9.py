class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()
        res = []

        for r in range(len(nums)):
            while mono_q and nums[mono_q[-1]] < nums[r]:
                mono_q.pop()
            mono_q.append(r)

            if mono_q[0] <= r - k:
                mono_q.popleft()

            if r >= k - 1:
                res.append(nums[mono_q[0]])

        return res
