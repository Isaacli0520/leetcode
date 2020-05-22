class Solution:
    # Recursive
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[]]
        for n in set(nums):
            tmp = list(nums)
            tmp.remove(n)
            for p in self.permuteUnique(tmp):
                res.append([n] + p)
        return res
    
    # Backtracking
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def dfs(ls, idx):
            if idx == l - 1:
                res.append(ls)
            for n in set(ls[idx:]):
                # Remove element from remaining 
                # and put at current **only once**
                remaining = list(ls[idx:])
                remaining.remove(n)
                dfs(ls[:idx] + [n] + remaining, idx + 1)
        dfs(nums, 0)
        return res

    # Swap with sorted list
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def dfs(ls, idx):
            if idx == l - 1:
                res.append(ls)
            for i in range(idx, l):
                # Skip Duplicates
                if i > idx and ls[i] == ls[idx]:
                    continue
                # Put duplicates at front only once
                ls[idx], ls[i] = ls[i], ls[idx]
                dfs(list(ls), idx + 1)
        nums.sort()
        dfs(nums, 0)
        return res
        
    
    