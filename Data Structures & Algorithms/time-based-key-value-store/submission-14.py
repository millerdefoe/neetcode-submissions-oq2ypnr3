from collections import deque

class TimeMap:

    def __init__(self):
        self.key_to_list = defaultdict(list) #key -> list 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_list[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.key_to_list[key]) == 0:
            return ""
        values = self.key_to_list[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        
        
