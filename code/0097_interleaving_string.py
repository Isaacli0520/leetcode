class Solution:
    # DP
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def helper(i, j):
            k = i + j
            if k == len(s3):
                return True
            if i == len(s1):
                return s3[k:] == s2[j:]
            if j == len(s2):
                return s3[k:] == s1[i:]
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            if s1[i] == s3[k]:
                res |= helper(i + 1, j)
            if s2[j] == s3[k]:
                res |= helper(i, j + 1)
            dp[(i, j)] = res
            return res
        
        return helper(0, 0)