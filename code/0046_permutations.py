class Solution:
    # Dfs
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, track):
            if len(track) == len(nums):
                res.append(track)
                return
            for i in range(len(nums)):
                # O(n); Can use a hashtable to reduce to O(1)
                if nums[i] not in track:
                    helper(nums, track + [nums[i]])
        helper(nums, [])
        return res
    
    
    # Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(l):
            if l == n - 1:
                res.append(list(nums))
                return
            for i in range(l, n):
                # Fix current position l with value from l to n
                nums[l], nums[i] = nums[i], nums[l]
                # Permute next position
                dfs(l + 1)
                # Restore
                nums[l], nums[i] = nums[i], nums[l]
        dfs(0)
        return res
        