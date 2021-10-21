class Solution:
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
    
    # Faster than dp
    def longestPalindrome(self, s: str) -> str:
        max_len, max_start = 0, 0
        mid = 0
        l = len(s)
        while mid < l:
            # start from mid
            left, right = mid, mid
            
            # skip duplicates and count for even length palindromes
            while right < l - 1 and s[right + 1] == s[right]:
                right = right + 1
                
            # mid move to next position
            # skip duplicates automatically
            mid = right + 1
            
            # Find longest palindrome given current mid
            while left > 0 and right < l - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            
            # Record longest palindrom length and start for return
            if right - left + 1 > max_len:
                max_len = right - left + 1
                max_start = left
        
        return s[max_start:max_start + max_len]
            
        
            
            
            
            