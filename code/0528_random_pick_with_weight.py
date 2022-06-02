class Solution:
    # Presum array: length of len(w) + 1
    def __init__(self, w: List[int]):
        self.presum = [0]
        for weight in w:
            self.presum.append(self.presum[-1] + weight)

    # Example:
    #    idx: N, 0, 1, 2, 3, 4, 5
    #      w: 1, 3, 2, 4, 5
    # presum: 0, 1, 4, 6, 10, 15
    # Random value: 3
    # Binary search result: idx 2 of presum array
    # Actual idx: 1
    # Therefore, returns mid or left - 1
    def pickIndex(self) -> int:
        # Random number of range [1, self.presums[-1]]
        target = random.randint(0, self.presum[-1] - 1)
        left, right = 0, len(self.presum)
        # Binary search
        # Returns the minimum value's idx that is
        # bigger than target
        while left < right:
            mid = left + (right - left) // 2
            if target == self.presum[mid]:
                return mid
            elif target < self.presum[mid]:
                right = mid
            else:
                left = mid + 1
        return left - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()