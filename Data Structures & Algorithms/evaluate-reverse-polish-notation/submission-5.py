class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack
        s = []
        i = 0
        operator = {'/','+','*','-'}
        while i < len(tokens):
            
            if tokens[i] in operator:
                num2 = s.pop()
                num1 = s.pop()
                res = 0
                if tokens[i] == '/':
                    res = int(num1 / num2)
                if tokens[i] == '+':
                    res = num1 + num2
                if tokens[i] == '*':
                    res = num1 * num2
                if tokens[i] == '-':
                    res = num1 - num2
                s.append(res)
            else:
                s.append(int(tokens[i]))
            i += 1
        
        return s.pop()
