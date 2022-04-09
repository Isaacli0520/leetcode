class Solution:
    # Quick Select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, mid, right = [], [], []
        pivot = random.choice(nums)
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            elif num < pivot:
                right.append(num)
        
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k <= len(left) + len(mid):
            return mid[0]
        else:
            return self.findKthLargest(right, k - len(left) - len(mid))