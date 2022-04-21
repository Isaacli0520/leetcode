class Solution:
    # Decreasing Monotonic Stack
    # Extend array to twice its size to solve the circular case
    # And we don't need to really extend the array
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [0] * n
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if not stack:
                res[i % n] = -1
            else:
                res[i % n] = stack[-1]
            stack.append(nums[i % n])
        return res