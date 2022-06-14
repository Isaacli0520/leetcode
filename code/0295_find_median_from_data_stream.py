class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    # Case 1: len(self.small) > len(self.large)
    #   We want to push to large. To make sure the value pushed to large
    #   really belongs to large, we have to push it to small first, and 
    #   pop the largest from small. 
    # Case 2: len(self.small) <= len(self.large)
    #   Similar case. Push to large first, and pop the smallest from large
    def addNum(self, num: int) -> None:
        if len(self.small) > len(self.large):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()