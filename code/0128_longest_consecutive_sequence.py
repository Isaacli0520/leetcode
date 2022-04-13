class Solution:
    # Hash table (Python set is implemented with hash table)
    # set lookup O(1)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxi = 0
        for num in nums:
            # If this is the start of a streak a, a + 1, a + 2...
            if num - 1 not in nums:
                i = num + 1
                while i in nums:
                    i += 1
                maxi = max(maxi, i - num)
        return maxi
            
    
    # Union Find
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uf = {}
        sizes = {}
        maxi = 1
        
        def find(x):
            x = uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def connect(a, b):
            nonlocal maxi
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if sizes[pa] > sizes[pb]:
                uf[pb] = pa
                sizes[pa] += sizes[pb]
                maxi = max(maxi, sizes[pa])
            else:
                uf[pa] = pb
                sizes[pb] += sizes[pa]
                maxi = max(maxi, sizes[pb])
        
        for num in nums:
            if num not in sizes:
                sizes[num] = 1
                uf[num] = num
            
            if num + 1 in uf:
                connect(num + 1, num)
            if num - 1 in uf:
                connect(num - 1, num)
        
        return maxi
        