class Solution:
    # Naive DP
    def __init__(self):
        self.dp = {}
        
    def numDecodings(self, s: str) -> int:
        if s in self.dp:
            return self.dp[s]
        if len(s) <= 1:
            ret =  int(s != "0")
        else: 
            ret = (self.numDecodings(s[1:]) if s[0] != "0" else 0) + (self.numDecodings(s[2:]) if s[0] != "0" and 0 < int(s[:2]) < 27 else 0)
        self.dp[s] = ret
        return ret


    # O(1) DP
    def numDecodings(self, s: str) -> int:
        curr, prev, prev_d = int(s > ''), 0, ''
        for d in s:
            prev, prev_d, curr = curr, d, (d > '0')*curr + (9 < int(prev_d + d) < 27)*prev
        return curr