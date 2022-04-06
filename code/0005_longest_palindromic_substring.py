class Solution:
    # Two Pointers? 
    # For every i
    # search for palindrom with s[i] as mid
    # search for palindrom with s[i], s[i + 1] as mid
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)):
            res = max(res, self.helper(s, i - 1, i + 1), self.helper(s, i, i + 1), key=len)
        return res

    def helper(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


    # Dynamic Programming
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]
        max_len = 0
        max_start = 0
        # Start = l - 1 to 0
        for i in range(l - 1, -1, -1):
            # End = Start to l - 1
            for j in range(i, l):
                # j - 2 <= 2 : "aba" or "aa" or "a"
                #               012      01      0
                # dp[i + 1][j - 1] : "abba" => "bb" and "a" == "a"
                #                     0123      12
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_start = i
        return s[max_start:max_start + max_len]
            
        
            
            
            
            