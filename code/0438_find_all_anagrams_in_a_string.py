from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        
        target = Counter(p)
        window = Counter(s[:n])
        
        res = []
        if target == window:
            res.append(0)
            
        for i in range(len(s) - n):
            left_c = s[i]
            right_c = s[i + n]
            
            if window[left_c] == 1:
                del window[left_c]
            else:
                window[left_c] -= 1
            
            if right_c in window:
                window[right_c] += 1
            else:
                window[right_c] = 1
            
            if window == target:
                res.append(i + 1)
        return res