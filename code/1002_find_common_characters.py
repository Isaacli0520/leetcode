class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = defaultdict(int)
        for i in range(26):
            res[chr(i + 97)] = 101
            
        for word in words:
            c = Counter(word)
            for k in res:
                res[k] = min(res[k], c[k])
            
        ans = []
        for k, v in res.items():
            if v != 101 and v > 0:
                ans += [k] * v
        return ans