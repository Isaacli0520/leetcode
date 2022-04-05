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
        window = defaultdict(int)
        left = 0
        res = 0
        
        for right in range(len(s)):
            right_c = s[right]
            window[right_c] += 1
            
            while window[right_c] > 1:
                left_c = s[left]
                left += 1
                window[left_c] -= 1
            res = max(res, right - left + 1)
        return res
                
            