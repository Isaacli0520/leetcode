class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
        