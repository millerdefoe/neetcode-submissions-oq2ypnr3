class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        index = 0
        while index < len(s):
            if stack and stack[-1][0] == s[index]:
                count = stack[-1][1] + 1
            else:
                count = 1
            stack.append((s[index], count))
            index += 1
            if count == k:
                for _ in range(k):
                    stack.pop()



        return "".join(char for char,count in stack)