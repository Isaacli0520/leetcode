class Solution:
    # O(N) (O(2N))
    # def frequencySort(self, s: str) -> str:
    #     res = ""
    #     c = Counter(s)
    #     d = defaultdict(list)
    #     for k, v in c.items():
    #         d[v].append(k)
    #     maxi = max(c.values())
    #     for i in range(maxi, 0, -1):
    #         if i in d:
    #             for v in d[i]:
    #                 res += i * v
    #     return res
            
    # O(N + klogk) where k=62 (a-zA-Z0-9) 
    def frequencySort(self, s: str) -> str:
        res = ""
        c = Counter(s)
        for i, cnt in sorted(c.items(), key=lambda x:-x[1]):
            res += i * cnt
        return res