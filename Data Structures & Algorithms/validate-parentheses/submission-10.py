class Solution:
    def isValid(self, s: str) -> bool:
        holder = []
        for i in s:
            if i == '(':
                holder.append(i)
            elif i == '[':
                holder.append(i)
            elif i == '{':
                holder.append(i)
            else:
                if i == '}' and holder and holder[-1] == '{':
                    holder.pop()
                elif i == ']' and holder and holder[-1] == '[':
                    holder.pop()            
                elif i == ')' and holder and holder[-1] == '(':
                    holder.pop()
                else:
                    return False

        if holder:
            return False
        return True
