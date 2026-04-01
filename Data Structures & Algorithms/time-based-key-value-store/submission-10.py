class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        keyStack = self.tMap.get(key, [])
        keyStack.append((value, timestamp))
        self.tMap[key] = keyStack

    def get(self, key: str, timestamp: int) -> str:

        if (key in self.tMap):
            l, r = 0, len(self.tMap[key])
            res = -1
            while l < r:
                m = l +((r-l) // 2)
                if self.tMap[key][m][1] <= timestamp:
                    l = m + 1
                    res = max(res, m)
                else:
                    r = m
            
            if self.tMap[key][res][1] <= timestamp:
                return self.tMap[key][res][0]
        
        return ""
