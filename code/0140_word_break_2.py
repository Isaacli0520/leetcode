class Solution:
    # Backtracking
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        res = []
        
        def helper(path, start):
            if start == n:
                res.append(" ".join(path))
                return
            
            for end in range(start + 1, n + 1):
                ss = s[start:end]
                if ss in words:
                    path.append(ss)
                    helper(path, end)
                    path.pop()
        
        helper([], 0)
        return res