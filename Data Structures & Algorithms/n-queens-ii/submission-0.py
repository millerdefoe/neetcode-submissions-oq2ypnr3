class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag_diff = set()
        diag_sum = set()
        res = 0
        
        def dfs(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if c in cols or (r + c) in diag_sum or (r - c) in diag_diff:
                    continue
                
                cols.add(c)
                diag_diff.add(r - c)
                diag_sum.add(r + c)

                dfs(r + 1)

                cols.remove(c)
                diag_diff.remove(r - c)
                diag_sum.remove(r + c)

        dfs(0)

        return res





