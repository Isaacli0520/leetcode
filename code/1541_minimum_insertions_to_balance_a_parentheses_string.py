class Solution:
    def minInsertions(self, s: str) -> int:
        need = 0
        cnt = 0
        for c in s:
            if c == "(":
                if need % 2 == 1:
                    cnt += 1
                    need -= 1
                need += 2
            elif c == ")":
                need -= 1
                if need == -1:
                    cnt += 1
                    need = 1
        return cnt + need