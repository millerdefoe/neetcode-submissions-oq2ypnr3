class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canContain(size, contMax, numList):
            curSize = size
            cont = 1
            for i in range(len(numList)):
                if curSize - numList[i] < 0:
                    cont += 1
                    curSize = size - numList[i]
                else:
                    curSize -= numList[i]
            
            if cont <= contMax:
                return True
            else:
                return False
            
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = l + ((r-l) // 2)
            print(m)
            if canContain(m, k, nums):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
