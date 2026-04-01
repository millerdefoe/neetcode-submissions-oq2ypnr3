class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def findPeak() -> int:
            l, r = 0, mountainArr.length() - 1
            while l <= r:
                m = l + ((r-l) // 2)
                if mountainArr.get(m-1) < mountainArr.get(m) > mountainArr.get(m + 1):
                    return m
                elif mountainArr.get(m-1) < mountainArr.get(m) < mountainArr.get(m + 1):
                    l = m + 1
                else:
                    r = m - 1
        
        #now we know peak, search left then right for solution.
        l, r = 0, findPeak()
        print(findPeak())

        while l <= r:
            m = l + ((r-l) // 2)
            if mountainArr.get(m) < target:
                l = m + 1
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                return m
        
        l, r = findPeak() + 1, mountainArr.length() - 1
        while l <= r:
            m = l + ((r-l) // 2)
            if mountainArr.get(m) > target:
                l = m + 1
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                return m

        return -1