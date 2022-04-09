class Solution:
    # Naive
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [i for i, j in sorted(count.items(), key=lambda x:x[1], reverse=True)[:k]]
    
    # Bucket Sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = collections.defaultdict(list)
        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for freq in range(len(nums), -1, -1):
            res += buckets[freq]
            if len(res) >= k:
                return res[:k]
            
        return res[:k]
        