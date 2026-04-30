class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.window_sum = 0
        self.size = size
        


    def next(self, val: int) -> float:

        self.queue.append(val)
        remove = 0
        if len(self.queue) > self.size:
            remove = self.queue.popleft()
        
        self.window_sum = self.window_sum - remove + val

        return self.window_sum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
