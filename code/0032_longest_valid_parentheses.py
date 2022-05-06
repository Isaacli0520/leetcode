class Solution:
    # Match longest valid parentheses continuously
    # Keep a dp array that tracks the longest valid parentheses until
    # index i. (For cases like ")()())")
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        maxi = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    left_index = stack.pop()
                    dp[i + 1] = i - left_index + 1 + dp[left_index]
                    maxi = max(maxi, dp[i + 1])
        return maxi

    # No Stack
    def longestValidParentheses(self, s: str) -> int:
        max_len, open_p = 0, 0
        # Dp[i] represents longest length matches to current index
        dp = [0 for i in range(len(s))]
        
        for i in range(len(s)):
            if s[i] == "(":
                open_p += 1
            # Matches Found
            if s[i] == ")" and open_p > 0:
                open_p -= 1
                
                # Update dp[i] b/c "(" and ")" are found 
                dp[i] = dp[i - 1] + 2
                
                # Count previous matches
                # Example: ()(())
                #          012345
                #
                # V[5] = V[4] + 2 = 2 + 2 = 4
                # V[1] not counted
                #
                # should count V[5 - V[5]] = V[5 - 4] = V[1] because 
                # the last V[5] = 4 characters must be valid parentheses
                # and V[1] is not counted for V[4] due to S[2] == "("
                if i - dp[i] > 0:
                    dp[i] += dp[i - dp[i]]
                
                # Update Longest Length
                max_len = max(max_len, dp[i])
                
        return max_len
                