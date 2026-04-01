class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operands = ['+', '-', '/', '*']
        for r in tokens:
            if r not in operands:
                numStack.append(int(r))
            else:
                if r == '+':
                    val1 = numStack.pop()
                    numStack.append(val1 + numStack.pop())
                elif r == '-':
                    val1 = numStack.pop()
                    numStack.append(numStack.pop() - val1)
                elif r == '/':
                    val1 = numStack.pop()
                    numStack.append(int(numStack.pop() / val1))
                elif r == '*':
                    val1 = numStack.pop()
                    numStack.append(numStack.pop() * val1)

        return numStack.pop()