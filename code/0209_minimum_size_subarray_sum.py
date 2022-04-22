class Solution:
    # O(n), Sliding Window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = 0
        l = 0
        mini = len(nums) + 1
        for r in range(len(nums)):
            tot += nums[r]
            while tot >= target:
                mini = min(mini, r - l + 1)
                tot -= nums[l]
                l += 1
        # return 0 if mini == len(nums) + 1 else mini
        return mini % (len(nums) + 1)

    # O(nlogn), Prefix Sum + Binary Search
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums) + 1
        left = 0
        for i, n in enumerate(nums[1:], 1):
            nums[i] = nums[i - 1] + n
        for right, n in enumerate(nums):
            if n >= s:
                target = n - s
                l, r = left, right
                while l < r:
                    mid = l + (r - l) // 2
                    if nums[mid] <= target:
                        l = mid + 1
                    elif nums[mid] > target:
                        r = mid
                left = l
                result = min(result, right - left + 1)
        return result if result != len(nums) + 1 else 0
        