import random
class RandomizedSet:

    # Keep a dict to record the idx of each element
    def __init__(self):
        self.d = {}
        self.ls = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = self.length
        self.ls.append(val)
        self.length += 1
        return True

    # Instead of removing the element in the middle
    # of the list and move every element, we can swap
    # the element with the last element and pop the last
    # element. Remember to update the dict.
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        self.d[self.ls[-1]], self.ls[self.d[val]]= self.d[val], self.ls[-1]
        del self.d[val]
        self.ls.pop()
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.ls)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()