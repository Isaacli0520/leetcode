class Solution:
    # DP O(n^2)
    # 
    # nums = [0, 1, 0, 3, 2, 3]
    # dp[n] = longest subseq length ended with nums[n]
    # dp[n] = 1 + max([ dp[m] for m in nums_less_than_nums[n] ])
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    # Binary Search O(nlog(n))
    def lengthOfLIS(self, nums: List[int]) -> int:
        tops = []
        for i in range(len(nums)):
            card = nums[i]
            left, right = 0, len(tops)
            while left < right:
                mid = left + (right - left) // 2
                if tops[mid] < card:
                    left = mid + 1
                elif tops[mid] >= card:
                    right = mid
            # Create new pile
            if left == len(tops):
                tops.append(card)
            # Place on the leftmost possible pile
            else:
                tops[left] = card
        return len(tops)