class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dfs with memoisation
        cache = {}

        def dfs(day):
            if day >= len(days):
                return 0
            if day in cache:
                return cache[day]
            
            cache[day] = float("inf")
            j = day
            for cost, duration in zip(costs, [1,7,30]):
                j = day
                while j < len(days) and days[j] < days[day] + duration:
                    j += 1
                
                cache[day] = min(cache[day], cost + dfs(j))
            return cache[day]

        
        return dfs(0)