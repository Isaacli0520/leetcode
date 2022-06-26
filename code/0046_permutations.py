class Solution:
    # Classic Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(ls, path):
            if not ls:
                res.append(path[:])
            for i in range(len(ls)):
                path.append(ls[i])
                helper(ls[:i] + ls[i + 1:], path)
                path.pop()
        helper(nums, [])
        return res

    # Use visited arr instead of creating new ones
    def permute(self, nums: List[int]) -> List[List[int]]:
            res = []
            visited = [False] * len(nums)
            def helper(path):
                if len(path) == len(nums):
                    res.append(path[:])
                    return
                for i in range(len(nums)):
                    if not visited[i]:
                        path.append(nums[i])
                        visited[i] = True
                        helper(path)
                        path.pop()
                        visited[i] = False
            helper([])
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
        