class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxi = 0
        for c in s:
            if c == "(":
                depth += 1
            elif c == ")":
                maxi = max(depth, maxi)
                depth -= 1
        return maxi