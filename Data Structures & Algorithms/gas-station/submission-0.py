class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        i = 0
        gasBal = 0
        start = i
        dist =0
        while dist < len(gas):
            gasBal += gas[i]
            gasBal -= cost[i]
            dist += 1
            i += 1
            if dist == len(gas):
                break
            if i == len(gas):
                i = 0
            if gasBal < 0:
                gasBal = 0
                dist = 0
                start = i
            
        return start