# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nl = deque(nestedList)
    
    def next(self) -> int:
        return self.nl.popleft().getInteger()
    
    # Assuming hasNext() is called exactly one time before each next() call
    def hasNext(self) -> bool:
        while len(self.nl) > 0 and not self.nl[0].isInteger():
            item = self.nl.popleft().getList()
            self.nl.extendleft(item[::-1])
        return len(self.nl) > 0
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())