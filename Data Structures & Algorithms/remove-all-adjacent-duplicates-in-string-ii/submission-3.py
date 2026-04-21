class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        index = 0
        while index < len(s):
            stack.append(s[index])
            index += 1
            if len(stack) >= k:
                remove = True
                for i in range(1, k + 1):
                    if stack[-1] != stack[-i]:
                        remove = False
                        break
                if remove:
                    for _ in range(k):
                        stack.pop()


        return "".join(stack)