class Solution:
    # DP Optimized
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, up_prev = 1, 1
        down, down_prev = 1, 1
        for i in range(1, len(nums)):
            # Going up
            if nums[i] > nums[i - 1]:
                up = down_prev + 1
                down = down_prev
                up_prev = up
            elif nums[i] == nums[i - 1]:
                up = up_prev
                down = down_prev
            # Going down
            elif nums[i] < nums[i - 1]:
                down = up_prev + 1
                up = up_prev
                down_prev = down
        return max(down, up)
    
    # DP
    # up[i] = longest length of wiggle subseq ended at nums[i] that expects a rising wiggle after this 
    # down[i] = ... that expects a down wiggle after this
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [1] * len(nums)
        down = [1] * len(nums)
        for i in range(1, len(nums)):
            # Going up
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] == nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
            # Going down
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
        return max(down[-1], up[-1])
    
    # Greedy
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = None
        res = 1
        # We only want local minimum and maximum
        #             7*
        #           6   5   
        #     5*  5       
        #   2   4*           4*
        # 1*              3*
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                up = True
                res += 1
            elif nums[i] < nums[i - 1] and up != False:
                up = False
                res += 1
        return res