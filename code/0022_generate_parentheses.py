class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(curr, op, ed):
            if op == n and ed == n:
                res.append("".join(curr))
            if op < n:
                curr.append('(')
                helper(curr, op + 1, ed)
                curr.pop()
            if op > ed:
                curr.append(')')
                helper(curr, op, ed + 1)
                curr.pop()
        helper([], 0, 0)
        return res