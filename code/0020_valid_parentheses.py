class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack or stack[-1] != d[c]:
                    return False
                stack.pop()
        return not stack