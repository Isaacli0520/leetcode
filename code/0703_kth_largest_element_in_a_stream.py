class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        for num in nums:
            heapq.heappush(self.hp, num)
            if len(self.hp) > k:
                heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)