class Solution:
    # Monotonic Queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        
        # Decreasing monotonic queue
        def add_to_queue(q, ele):
            while q and q[-1] < ele:
                q.pop()
            q.append(ele)
        
        # ele may have been poped during previous add
        def pop_from_queue(q, ele):
            if ele == q[0]:
                q.popleft()
            
        for i in range(len(nums)):
            add_to_queue(queue, nums[i])
            # Start counting max after queue is filled at least k elements
            if i >= k - 1: 
                res.append(queue[0])
                pop_from_queue(queue, nums[i - k + 1])
        return res