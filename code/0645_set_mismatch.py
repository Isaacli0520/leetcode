class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                break
        return res
            