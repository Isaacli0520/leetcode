from collections import defaultdict
class Solution:
    # Record last pos of every char
    # if new char is in last_pos, move start to
    # last_pos[new_char] + 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        start = 0
        res = 0
        for i, c in enumerate(s):
            if c in last_pos and start <= last_pos[c]:
                start = last_pos[c] + 1
            res = max(res, i - start + 1)
            last_pos[c] = i
        return res
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        d = defaultdict(int)
        l = 0
        maxi = 1
        for r in range(len(s)):
            d[s[r]] += 1
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            maxi = max(maxi, r - l + 1)
        return maxi
                
            