class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        cnt = 0
        for c in s:
            if c == "(":
                need += 1
            elif c == ")":
                if need == 0:
                    cnt += 1
                else:
                    need -= 1
        return need + cnt