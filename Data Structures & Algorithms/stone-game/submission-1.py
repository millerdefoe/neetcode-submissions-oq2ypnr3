class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp = {}
        #even turn is alice, odd turn is bob

        def dfs(s, e, turns):
            if turns == len(piles):
                return 0
            if s > e:
                return 0

            if (s, e, turns) in dp:
                return dp[(s, e, turns)]
            
            if turns % 2 == 0:
                total = max(dfs(s+1, e, turns + 1) + piles[s], dfs(s, e-1, turns + 1) + piles[e]) 
            else:
                total = min(dfs(s+1, e, turns + 1) - piles[s], dfs(s, e-1, turns + 1) - piles[e]) 
            
            dp[(s, e, turns)] = total
            return total

        return True if dfs(0, len(piles)-1, 0) > 0 else False