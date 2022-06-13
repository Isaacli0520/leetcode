class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] += 1
        for i, c in enumerate(s):
            if arr[ord(c) - 97] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
        