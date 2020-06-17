class Solution:
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
    
    # Greedy
    def jump(self, nums):
        steps = 0
        curr_jmp_max, prev_jmp_max = 0, 0
        for i in range(len(nums) - 1):
            curr_jmp_max = max(curr_jmp_max, i + nums[i])
            # if we reaches the previous maximum point we can get to
            # it means that we have to increase step by 1 to reach
            # further points
            if i == prev_jmp_max:
                steps += 1
                prev_jmp_max = curr_jmp_max
        return steps
  