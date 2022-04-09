import random
class Solution:
    # Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        l, r = 0, 0
        res = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        if l < len(left):
            res += left[l:]
        if r < len(right):
            res += right[r:]
        return res
    
    # Quick Sort O(n) space
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        return self.sortArray(left) + mid + self.sortArray(right)

    # Quick Sort In place
    def sortArray(self, nums: List[int]) -> List[int]:
        random.shuffle(nums)
        
        def helper(lo, hi):
            if lo >= hi:
                return
            i, j = lo, hi
            pivot = nums[random.randint(lo, hi)]
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                # nums[i] >= pivot and nums[j] <= pivot
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            helper(lo, j)
            helper(i, hi)
            
        helper(0, len(nums) - 1)
        return nums
    
    # Bubble Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums