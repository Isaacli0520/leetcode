class Solution:
    # Heap
    # O(n + nlogk) 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        hp = []
        for num, freq in c.items():
            heapq.heappush(hp, (freq, num))
            if len(hp) > k:
                heapq.heappop(hp)
        return [item[1] for item in hp]
    
    
    # Bucket Sort
    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        bucket = defaultdict(list)
        for num, freq in c.items():
            bucket[freq].append(num)
        
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in bucket:
                res += bucket[freq]
                if len(res) >= k:
                    return res[:k]
        # return res[:k]