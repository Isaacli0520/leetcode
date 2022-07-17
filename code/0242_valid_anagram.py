class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [0] * 26
        for c in s:
            ls[ord(c) - 97] += 1
        for c in t:
            ls[ord(c) - 97] -= 1
        for i in ls:
            if i != 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
        return len(d) == 0