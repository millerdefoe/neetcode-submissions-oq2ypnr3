class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        houses = len(costs) -1
        #index [0,1,2] == R B G 
        res = float("inf")
        self.hMap = {}
        def dfs(house, pColor):
            if house == -1:
                return 0
            
            if (house, pColor) in self.hMap:
                return self.hMap[(house, pColor)]

            value = float("inf")
            for i in range(3):
                if i != pColor:
                    value = min(value, costs[house][i] + dfs(house - 1, i))
                    

            self.hMap[(house, pColor)] = value
            return value
                    
        return dfs(houses, 4)

            
            