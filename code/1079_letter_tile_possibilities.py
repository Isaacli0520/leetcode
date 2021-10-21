class Solution:
    # Backtracking 1
    def numTilePossibilities(self, tiles: str) -> int:
        l = len(tiles)
        res = []
        def helper(nums, idx):
            res.append("".join(nums[:idx]))
            for num in set(list(nums[idx:])):
                remaining = list(nums[idx:])
                remaining.remove(num)
                helper(list(nums[:idx]) + [num] + remaining, idx + 1)
        helper(tiles, 0)
        return len(res) - 1
    
    # Backtracking 2
    def numTilePossibilities(self, tiles: str) -> int:
        l = len(tiles)
        res = []
        
        def dfs(ls, idx):
            res.append(ls[:idx])
            for i in range(idx, l):
                if i > idx and ls[i] == ls[idx]:
                    continue
                ls[idx], ls[i] = ls[i], ls[idx]
                # Remember to use list(ls) to create a new list
                dfs(list(ls), idx + 1)
                
        tiles = sorted(list(tiles))
        dfs(tiles, 0)
        return len(res) - 1
            