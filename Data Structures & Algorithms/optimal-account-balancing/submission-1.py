from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        balance_map = defaultdict(int)
        for a, b, amount in transactions:
            balance_map[a] += amount
            balance_map[b] -= amount

        balance_array = list(balance_map.values())
        
        def dfs(i):
            res = float("inf")
            while i < len(balance_array) and balance_array[i] == 0:
                i += 1
            if i == len(balance_array):
                return 0
            
            for j in range(i, len(balance_array)):
                if balance_array[i] * balance_array[j] < 0:
                    balance_array[j] += balance_array[i]
                    res = min(dfs(i+1) + 1, res)
                    balance_array[j] -= balance_array[i]
            return res
        return dfs(0)

            