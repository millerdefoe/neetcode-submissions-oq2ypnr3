class StockSpanner:

    def __init__(self):
        self.sList = []
        self.tStack = [] #(index, price)
        self.i = 0

    def next(self, price: int) -> int:
        print(self.tStack)
        self.sList.append(price)
        while self.tStack and self.tStack[-1][1] <= price:
            self.tStack.pop()
        if self.tStack:
            val = self.i - self.tStack[-1][0]
        else:
            val = self.i + 1
        self.tStack.append([self.i, price])
        self.i += 1

        return val



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)