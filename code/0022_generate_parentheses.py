class Solution:
    # Backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(path, op, close):
            if op == n and close == n:
                res.append("".join(path[:]))
            chars = []
            if op < n:
                chars.append(("(", 1, 0))
            if close <  op:
                chars.append((")", 0, 1))
            for ch, a, b in chars:
                path.append(ch)
                helper(path, op + a, close + b)
                path.pop()

        helper([], 0, 0)
        return res