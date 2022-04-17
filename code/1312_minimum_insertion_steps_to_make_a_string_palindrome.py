class Solution:
    # DP
    # dp[i][j] = min steps to make s[i:j + 1] palindrome
    # if s[i] == s[j]:
    #   dp[i][j] = dp[i + 1][j - 1]
    # else:
    #   dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
    def minInsertions(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        
        return dp[0][len(s) - 1]
                
        