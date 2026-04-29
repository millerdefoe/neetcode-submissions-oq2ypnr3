class RandomizedSet:

    def __init__(self):
        self.hMap = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.hMap:
            return False
        self.hMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hMap:
            return False
        
        idx = self.hMap[val] 
        last = self.nums[-1] 
        self.nums[idx] = last
        self.hMap[last] = idx
        self.nums.pop()
        del self.hMap[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()