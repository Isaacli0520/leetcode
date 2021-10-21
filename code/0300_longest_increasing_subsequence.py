class Solution:
    # DP O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        result = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

    # Binary Search O(nlogn)                
    def lengthOfLIS(self, nums: List[int]) -> int:
        tops = []
        for i in range(len(nums)):
            card = nums[i]
            left, right = 0, len(tops)
            # insert every card
            while left < right:
                mid = left + (right - left) // 2
                if tops[mid] < card:
                    left = mid + 1
                elif tops[mid] > card:
                    right = mid
                elif tops[mid] == card:
                    right = mid
            # create new pile
            if left == len(tops): 
                tops.append(card)
            else:
                tops[left] = card
        # return number of piles
        return len(tops)
