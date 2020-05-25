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
                # Example no dup, idx = 0
                #  1   2  3  4  swap 2 1 
                # [2] [1] 3  4  swap 3 2
                # [3]  1 [2] 4  swap 4 3
                # [4]  1  2 [3] 
                # Example with dup, idx = 0
                #  1   2  3  3  4  swap 2 1 
                # [2] [1] 3  3  4  swap 3 2
                # [3]  1 [2] 3  4  skip 3 and swap 4 3
                # [4]  1  2 [3] 3
                # 3 is put to front for only once
                ls[idx], ls[i] = ls[i], ls[idx]
                # Remember use list(ls) to create new list
                dfs(list(ls), idx + 1)
        nums.sort()
        dfs(nums, 0)
        return res
        
    
    