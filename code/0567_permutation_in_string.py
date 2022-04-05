from collections import Counter
class Solution:
    # Fixed Length Window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        target = Counter(s1)
        window = Counter(s2[:n])
        
        if target == window:
            return True
        
        # Move fixed length window
        for i in range(len(s2) - n):
            left_c = s2[i]
            right_c = s2[i + n]
            if window[left_c] == 1:
                del window[left_c]
            else:
                window[left_c] -= 1
            
            if right_c in window:
                window[right_c] += 1
            else:
                window[right_c] = 1
            
            if window == target:
                return True
            
        return False
        
            