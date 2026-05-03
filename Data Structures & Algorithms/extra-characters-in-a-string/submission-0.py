class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        for word in dictionary:
            node = root
            for c in word:
                node = node.children[c]
            
            node.endOfWord = True
        
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.endOfWord:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res
        
        return dfs(0)
            