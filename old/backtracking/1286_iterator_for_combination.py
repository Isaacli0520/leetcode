import math
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.counter = 0
        self.last, self.end = None, characters[-combinationLength:]
        self.generator = self.generateNext(characters, [], combinationLength, 0)

    def generateNext(self,chars, path, combLen, idx):
        if combLen == 0:
            yield "".join(path)
            self.counter += 1
            return
        for i in range(idx, len(chars)):
            path.append(chars[i])
            yield from self.generateNext(chars, path,combLen - 1, i + 1)
            path.pop()
        
    
    def next(self) -> str:
        self.last = next(self.generator)
        return self.last
        

    def hasNext(self) -> bool:
        return self.last != self.end
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()