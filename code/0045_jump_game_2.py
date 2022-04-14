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
        
    # BFS
    # [2, 3, 1, 1, 4]
    # 1 step:
    #   index 1 and 2
    # 2 steps:
    #   index 3 and 4
    # For each step, update maxend based on every i + nums[i]
    # update start = end + 1, end = maxend
    def jump(self, nums: List[int]) -> int:
        l, start, end, step = len(nums), 0, 0, 0
        # end < l - 1 to cover the case when len(nums) == 1
        while end < l - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= l - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step
    