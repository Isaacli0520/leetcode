from random import randrange
class Solution:
    # Presum array: length of len(w) + 1
    def __init__(self, w: List[int]):
        presums = [0]
        for i, weight in enumerate(w):
            presums.append(weight + presums[i])
        self.presums = presums

    # Example:
    #    idx: N, 0, 1, 2, 3, 4, 5
    #      w: 1, 3, 2, 4, 5
    # presum: 0, 1, 4, 6, 10, 15
    # Random value: 3
    # Binary search result: idx 2 of presum array
    # Actual idx: 1
    # Therefore, returns mid - 1 or left - 1
    def pickIndex(self) -> int:
        # Random number of range [1, self.presums[-1]]
        target = randrange(1, self.presums[-1] + 1)
        left, right = 0, len(self.presums)
        # Binary search
        # Returns the minimum value's idx that is
        # bigger than target
        while left < right:
            mid = left + (right - left) // 2
            num = self.presums[mid]
            if target == num:
                return mid - 1
            elif target < num:
                right = mid
            elif target > num:
                left = mid + 1
        return left - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()