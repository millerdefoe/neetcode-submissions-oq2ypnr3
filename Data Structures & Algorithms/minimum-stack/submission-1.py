class MinStack:

    def __init__(self):
        self.stack = []
        self.monoStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monoStack:
            self.monoStack.append(val)
        elif val <= self.monoStack[-1]:
            self.monoStack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.monoStack[-1]:
            self.monoStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.monoStack[-1]
        
