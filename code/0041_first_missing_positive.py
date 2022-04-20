class Solution:
    # For an array of length n, the smallest missing positive
    # must be in the range [1, n + 1] 
    # Therefore, we ignore all values < 0 or > n by turning them into 0
    # For the rest nums, we put each num to its corresponding place
    # in the array, and find the first missing positive.
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] >= n + 1:
                nums[i] = 0
        for i in range(len(nums)):
            if nums[i] % (n + 1) > 0:
                nums[nums[i] % (n + 1) - 1] += n + 1
        for i in range(len(nums)):
            if nums[i] < n + 1:
                return i + 1
        return n + 1
                