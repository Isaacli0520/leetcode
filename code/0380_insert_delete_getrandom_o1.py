class RandomizedSet:

    def __init__(self):
        self.idxs = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.idxs:
            self.vals.append(val)
            self.idxs[val] = len(self.vals) - 1
            return True
        return False

    # Instead of removing the element in the middle
    # of the list and move every element, we can swap
    # the element with the last element and pop the last
    # element. Remember to update the dict.
    def remove(self, val: int) -> bool:
        if val not in self.idxs:
            return False
        
        rmv_idx = self.idxs[val]
        self.vals[rmv_idx] = self.vals[-1]
        self.idxs[self.vals[-1]] = rmv_idx
        del self.idxs[val]
        
        self.vals.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()