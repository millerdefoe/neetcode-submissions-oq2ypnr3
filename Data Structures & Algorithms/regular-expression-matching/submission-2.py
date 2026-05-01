class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            # Already computed this state
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: exhausted the pattern
            if j == len(p):
                return i == len(s)

            # Does the current pattern char match the current string char?
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Look ahead: is the NEXT pattern char a '*'?
            if j + 1 < len(p) and p[j + 1] == '*':
                # Choice 1: use '*' as zero occurrences — skip p[j] and p[j+1]
                # Choice 2: use one occurrence — consume s[i], stay at same j
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # No star — must match and advance both
                result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)