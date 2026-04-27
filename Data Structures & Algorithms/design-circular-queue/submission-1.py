class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.start = 0
        self.end = 0
        self.values = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.values == self.k:
            return False
        else:
            self.queue[self.end] = value
            self.end += 1
            self.end %= self.k
            self.values += 1
            return True

    def deQueue(self) -> bool:
        if self.values == 0:
            return False
        else:
            self.values -= 1
            self.queue[self.start] = -1
            self.start += 1
            self.start %= self.k
            return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.end - 1]

    def isEmpty(self) -> bool:
        return self.values == 0

    def isFull(self) -> bool:
        return self.values == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()