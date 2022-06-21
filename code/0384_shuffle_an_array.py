class Solution:

    def __init__(self, nums: List[int]):
        self.backup = nums[:]
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        self.nums = self.backup[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(self.n):
            rd = random.randint(i, self.n - 1)
            self.nums[i], self.nums[rd] = self.nums[rd], self.nums[i]
        return self.nums
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()