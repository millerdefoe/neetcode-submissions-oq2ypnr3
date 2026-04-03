
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {} #(i,j) = True / False
        def dfs(i,j):
             if j == len(p): 
                  return i == len(s)
             if (i,j) in dp:
                  return dp[(i,j)]
             currMatch = i < len(s) and (p[j] == s[i] or p[j] == '.')

             if j + 1 < len(p) and p[j+1] == '*':
                  dp[(i,j)] = dfs(i, j+2) or (currMatch and dfs(i+1, j))
             elif currMatch:
                  dp[(i,j)] = dfs(i+1, j+1)
             else:
                  dp[(i,j)] = False
             return dp[(i,j)]
        return dfs(0,0)
                  
           