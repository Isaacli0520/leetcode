class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def helper(s, track):
            if not s:
                res.append(track)
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    helper(s[i:], track + [s[:i]])
                    
        def isPalindrome(s):
            return s == s[::-1]
        
        helper(s, [])
        return res
            