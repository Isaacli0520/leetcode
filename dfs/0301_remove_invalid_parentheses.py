class Solution:
    # BFS
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            ctn = 0
            for char in s:
                if char == "(":
                    ctn += 1
                elif char == ")":
                    ctn -= 1
                    if ctn < 0:
                        return False
            return ctn == 0
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {st[:i] + st[i+1:] for st in level for i in range(len(st))}
    
    
    # DFS
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        def dfs(s, check, prev_i, prev_j):
            ctn, i = 0, prev_i
            while i < len(s) and ctn >= 0:
                if s[i] == check[0]:
                    ctn += 1
                if s[i] == check[1]:
                    ctn -= 1
                i += 1
                        
            # No extra ")" detected
            # Reverse to check if extra "(" exists
            if ctn >= 0:
                rvs = s[::-1]
                # if check[0] == "(", still need to check reverse
                if check[0] == "(":
                    dfs(rvs, [")","("], 0, 0)
                # if check[0] == ")" we have checked both directions
                # the string rvs is legal
                else:
                    res.append(rvs)
            # Extra ")" detected
            else:
                # s[i - 1] is the ")" that makes ctn < 0
                i -= 1
                for j in range(prev_j, i + 1):
                    # Skip duplicates
                    if s[j] == check[1] and (j == prev_j or s[j - 1] != check[1]):
                        dfs(s[:j] + s[j + 1:], check, i, j)
                
        dfs(s, ["(", ")"], 0, 0)
        return res
                