class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.array = []

    def insert(self, val: int) -> bool:
        res = val not in self.store
        if res:
            self.store[val] = len(self.array)
            self.array.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.store
        if res:
            last = self.array[-1]
            self.array[self.store[val]] = last
            self.array.pop()
            self.store[last] = self.store[val]
            del self.store[val]
        return res


    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()