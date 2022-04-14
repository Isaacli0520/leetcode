class Solution:
    # Backtracking
    # The key is to not do backtrack on the same element in 
    # current for loop.
    #
    # One way is to do "for x in set(ls)" instead of 
    # "for x in ls" and find the index of the element to remove it.
    # 
    # Another way is to use a Counter, which is a lot smarter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        cnt = Counter(nums)
        
        def helper(path):
            if len(path) == l:
                res.append(path[:])
                return
            for x in cnt:
                if cnt[x] > 0:
                    cnt[x] -= 1
                    path.append(x)
                    helper(path)
                    path.pop()
                    cnt[x] += 1
        helper([])
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
        
    
    