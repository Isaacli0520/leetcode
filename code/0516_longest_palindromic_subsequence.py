class Solution:
    # DP
    # dp[i][j] = longest palindrome subseq in str[i:j + 1]
    # if s[i - 1] == s[j - 1]
    #   dp[i][j] = dp[i + 1][j - 1] + 2
    # else
    #   dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        # Since for the state transitions, dp[i][j] is gonna depend
        # on dp[i + 1][j], dp[i + 1][j - 1], dp[i][j - 1], we need to
        # iterate backward for i and forward for j
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][len(s) - 1]
                