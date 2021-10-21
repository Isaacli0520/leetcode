class NumArray:

    def __init__(self, nums: List[int]):
        self.accum = [0] + nums
        for i in range(1, len(self.accum)):
            self.accum[i] += self.accum[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.accum[j + 1] - self.accum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)