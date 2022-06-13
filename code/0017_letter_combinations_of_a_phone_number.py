class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        # BFS
        idx = 0
        res = deque([""])
        while idx < len(digits):
            for i in range(len(res)):
                tmp = res.popleft()
                for c in d[digits[idx]]:
                    res.append(tmp + c)
            idx += 1
        return res
        
        # Backtracking
        res = []
        def helper(path, idx):
            if idx == len(digits):
                res.append("".join(path))
                return
            for c in d[digits[idx]]:
                path.append(c)
                helper(path, idx + 1)
                path.pop()
        helper([], 0)
        return res
            
                    