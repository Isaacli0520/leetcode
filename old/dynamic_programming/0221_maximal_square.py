class Solution:
    # O(n) space
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        if r == 0:
            return 0
        c = len(matrix[0])
        sz = 0
        # dp[i][j] stores maximum length of square up to point(i, j)
        dp = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                # If i == 0, j == 0, max length = 1 if matrix[i][j] == 1 else 0
                # If matrix[i][j] == 0, dp[i][j] = 0
                if not i or not j or matrix[i][j] == "0":
                    dp[i][j] = int(matrix[i][j])
                # 1 0 | 1       1 0 | 1
                # 1 1 | 1  ->   1 1 | 1
                # -------       -------
                # 1 1 | 1       1 1 | 2
                # Matrix        DP
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                sz = max(sz, dp[i][j])
        return sz * sz
    
    # O(c) space
    # Only need one row
    # Since for every row, we need 
    #
    # dp[i - 1][j] => current dp[j]
    # dp[i][j - 1] => dp[j - 1]
    # dp[i - 1][j - 1] => ??
    # 
    # Therefore, we have a variable "pre" that 
    # stores dp[i - 1][j - 1] e.g. current dp[j]
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        if r == 0:
            return 0
        c = len(matrix[0])
        sz, pre = 0, 0
        dp = [0 for j in range(c)]
        for i in range(r):
            for j in range(c):
                # Pre
                tmp = dp[j]
                if not i or not j or matrix[i][j] == "0":
                    dp[j] = int(matrix[i][j])
                # 1  0  | 1       1  0  | 1
                # 1 [1] | 1  ->   1 [1] | 1
                # ---------       ---------
                # 1  1  | 1       1  1  | 2
                # Matrix        DP
                else:
                    dp[j] = min(dp[j], dp[j - 1], pre) + 1
                sz = max(sz, dp[j])
                # Pre = dp[j] before change
                pre = tmp
        return sz * sz
    