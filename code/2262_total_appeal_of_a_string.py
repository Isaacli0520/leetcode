class Solution:
    def appealSum(self, s: str) -> int:
        # d marks the position + 1 of the last occurance of every
        # character. 
        # Example: god => godo
        #   org substrings:    d,  od,  god  =     1 + 2 + 3
        #   new substrings: o, do, odo, godo = 1 + 2 + 2 + 3 
        #
        #   only substrings that don't include 'o' will have
        #   an increase in distinct chars.
        #   Therefore, the new prev is 1 + i - d.get(s[i], 0)
        #   The best case is that the char never appeared before
        #   so we simply increase prev by 1 + i; but the worse
        #   case is when the chars appeared before, and we want
        #   to know its last occurance position
        d = {}
        d[s[0]] = 1
        res = 1
        prev = 1
        for i in range(1, len(s)):
            prev += 1 + i - d.get(s[i], 0)
            d[s[i]] = i + 1
            res += prev
        return res