class RandomizedCollection:

    def __init__(self):
        self.idxs = collections.defaultdict(set)
        self.vals = []

    # Keep a dict of {value: idxs in arr}
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idxs[val]:
            return False
        
        # Swap the value at last idx with a idx of val
        rmv_idx = self.idxs[val].pop()
        last = self.vals[-1]
        self.vals[rmv_idx] = last
        
        # Handles corner cases when rmv_idx == last index
        # Case 1: only 1 item in self.vals
        # Case 2: last element is the same as val, and the idx poped
        #         from the set is the same as the last idx
        if rmv_idx != len(self.vals) - 1:
            self.idxs[last].remove(len(self.vals) - 1)
            self.idxs[last].add(rmv_idx)

        # self.idxs[last].add(rmv_idx)
        # self.idxs[last].remove(len(self.vals) - 1)
        
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()