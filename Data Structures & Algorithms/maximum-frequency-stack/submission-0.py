class FreqStack:

    def __init__(self):
        self.stack = {}
        self.maxFreq = 0
        self.freqH = {}

    def push(self, val: int) -> None:
        valCnt = 1 + self.freqH.get(val, 0)
        self.freqH[val] = valCnt
        if valCnt > self.maxFreq:
            self.maxFreq = valCnt
            self.stack[valCnt] = []
        self.stack[valCnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.maxFreq].pop()
        self.freqH[res] -= 1
        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()