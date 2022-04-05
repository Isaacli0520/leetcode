import collections
class Solution:
    # Sliding Window
    def minWindow(self, s: str, t: str) -> str:
        # Maintain two dicts, one for window, one for target
        target = collections.defaultdict(int)
        for c in t:
            target[c] += 1
        window = {c:0 for c in t}
        left, right = 0, 0
        valid = 0
        best_s = ""
        # window is [left, right) (exclusive)
        while right < len(s):
            # Move right
            c = s[right]
            right += 1
            # Update valid if num of char c in window meets target
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    valid += 1
            # Move left to shrink window until there is not 
            # enough chars to meet target
            while len(target) == valid:
                # Record the best string
                if right - left < len(best_s) or best_s == "":
                    best_s = s[left:right]
                
                # Update valid
                c = s[left]
                left += 1
                if c in target:
                    if window[c] == target[c]:
                        valid -= 1
                    window[c] -= 1

        return best_s