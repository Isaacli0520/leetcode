class Solution:
    # DP
    # dp[m][k] = maximum number of floors we can check with k eggs and m moves
    # dp[m][k] = 1 + dp[m - 1][k - 1] + dp[m - 1][k]
    # we take 1 move to some floor (the first 1 in the equation)
    # if egg breaks
    #   the max number of floors we can check is dp[m - 1][k - 1]
    # if egg doesn't break
    #   the max number of floors we can check is dp[m - 1][k]
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            # If using m moves and K eggs can reach floor higher than N,
            # then m is the min move
            if dp[m][K] >= N:
                return m
        
        
    # DP brute force (TLE)
    def superEggDrop(self, k: int, n: int) -> int:
        dp = {}
        
        # drop egg at each floor i
        #
        # if it breaks: egg -= 1; search [1, i - 1] 
        # therefore using (egg - 1) eggs to deal with (i - 1) floors 
        # if it does not break: egg stays the same; search [i + 1, n]
        # therefore using (egg) eggs to deal with (n - i) floors 
        #
        # the maximum of both plus 1 is the number of moves since the
        # egg is gonna be either broken or unbroken.
        #
        # returns the min number of moves to determine the floor using 
        # (egg) number of eggs with (tot_floors) number of floors
        def helper(egg, tot_floors):
            # Base case
            if tot_floors == 0:
                return 0
            # Can only linearly search
            if egg == 1:
                return tot_floors
            
            if (egg, tot_floors) in dp:
                return dp[(egg, tot_floors)]
            
            mini = tot_floors
            for f in range(1, tot_floors + 1):
                mini = min(mini, 1 + max(helper(egg - 1, f - 1), helper(egg, tot_floors - f))) 
            dp[(egg, tot_floors)] = mini
            return mini
                
        return helper(k, n)
            