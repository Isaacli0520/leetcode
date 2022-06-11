class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        new_prefs = []
        for pref in preferences:
            new_pref = [0] * n
            for i, p in enumerate(pref):
                new_pref[p] = i
            new_prefs.append(new_pref)
        
        d_pairs = {}
        for a, b in pairs:
            d_pairs[a] = preferences[a][:new_prefs[a][b]]
            d_pairs[b] = preferences[b][:new_prefs[b][a]]
        
        res = 0
                        
        for a in d_pairs:
            for u in d_pairs[a]:
                if a in d_pairs[u]:
                    res += 1
                    break
        
        return res