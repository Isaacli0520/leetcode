class Solution:
    # Use min-heap: O(k + (n - k) * logk)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
    
    # Quick Select: Average O(n) Worst Case (On^2)
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