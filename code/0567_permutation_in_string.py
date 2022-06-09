from collections import Counter
class Solution:
    # Keep a variable to record matched characters
    # no need to check every key of target to see if 
    # current substring is a permutation of s1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = len(s1)
        target = Counter(s1)
        window = Counter()
        needed = len(target)
        
        matched = 0
        left, right = 0, 0
        
        while right < len(s2):
            new_char = s2[right]
            if new_char in target:
                window[new_char] += 1
                if window[new_char] == target[new_char]:
                    matched += 1
            right += 1
                    
            if right - left > l:
                old_char = s2[left]
                if old_char in target:
                    if window[old_char] == target[old_char]:
                        matched -= 1
                    window[old_char] -= 1
                left += 1
        
            if needed == matched:
                return True
            
        return False

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
        
            