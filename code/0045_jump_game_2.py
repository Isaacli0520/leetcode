class Solution:
    # Greedy
    # For curr number of jumps, search among all the possible 
    # positions we can get to for the farthest idx we can jump to.
    # 
    # Once we reach the end of the curr jump, we update the search range
    # to the farthest idx we found and repeat
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        curr_jump_end = 0
        # Do not include the last index, becasue if last_index == curr_jump_end,
        # jumps will be 1 more than what it's supposed to be
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_jump_end:
                jumps += 1
                curr_jump_end = farthest
                
        return jumps
        
    # DP
    # dp[i] = min number of jumps to reach index i
    def jump(self, nums: List[int]) -> int:
        curr_maxi = 0
        dp = list(range(len(nums)))
        for i, num in enumerate(nums):
            if num + i < curr_maxi:
                continue
            else:
                curr_maxi = num + i
            for j in range(1, min(num + 1, len(nums) - i)):
                dp[i + j] = min(dp[i] + 1, dp[i + j])
        return dp[-1]