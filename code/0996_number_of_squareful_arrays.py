import math
class Solution:
    # Backtracking
    def numSquarefulPerms(self, A: List[int]) -> int:
        l = len(A)
        res = []
        
        def helper(nums, idx):
            if idx == l:
                res.append(nums)
            for i in range(idx, l):
                if i > idx and nums[i] == nums[idx]:
                    continue
                nums[idx], nums[i] = nums[i], nums[idx]
                if idx == 0 or isSq(nums[idx] + nums[idx - 1]):
                    helper(list(nums), idx + 1)
                    
        def isSq(n):
            return n == math.isqrt(n) ** 2
        
        A.sort()
        helper(A, 0)
        return len(res)
    
    # Backtracking 2
    def numSquarefulPerms(self, A: List[int]) -> int:
        c = collections.Counter(A)
        # For every num in A, find candidates num in A such that
        # they add up to a Square
        cand = {i:{j for j in c if int((i + j) ** 0.5) ** 2 == (i + j)} for i in c}
        # Backtracking
        def dfs(x, left = len(A) - 1):
            c[x] -= 1
            count = sum([dfs(y, left - 1) for y in cand[x] if c[y]]) if left else 1
            c[x] += 1
            return count
        return sum(map(dfs, c))
            