class Solution:
    # DP
    # dp[i][j] = lcs between s1[:i] and s2[:j]
    # if s1[i - 1] == s2[j - 1]:
    #   dp[i][j] = 1 + dp[i - 1][j - 1]
    # else:
    #   dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in  range(l1 + 1)]
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # View Dp Matrix
        # print(" ".join([i for i in " #" + text2]))
        # tmp = "#" + text1
        # for i, row in enumerate(dp):
        #     print(tmp[i] + " " + " ".join([str(j) for j in row]))
            
        
        return dp[-1][-1]