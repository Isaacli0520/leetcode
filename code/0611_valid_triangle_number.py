class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        # If a <= b <= c, then a + b > c determines if its a triangle
        nums = sorted(nums)
        res = 0
        for l3 in range(2, len(nums)):
            l1, l2 = 0, l3 - 1
            while l1 < l2:
                # Decrease b, and see if a + b > c
                if nums[l1] + nums[l2] > nums[l3]:
                    res += l2 - l1
                    l2 -= 1
                # Increase a since a + b <= c
                else:
                    l1 += 1
        return res
                
        