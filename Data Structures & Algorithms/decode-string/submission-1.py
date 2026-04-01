class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        for i in s:
            if i == "]":
                while stack[-1] != "[":
                    cur = stack.pop() + cur
                cur[::-1]
                stack.pop() #remove [
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                stack.append(int(repeat) * cur)
                cur = ""
            else:
                stack.append(i)
            print(stack)

        return "".join(stack)