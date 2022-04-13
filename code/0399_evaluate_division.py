class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = {}
        
        def find(x):
            parent, ratio = uf.setdefault(x, (x, 1.0))
            if x != parent:
                new_parent, new_ratio = find(parent)
                uf[x] = (new_parent, ratio * new_ratio)
            return uf[x]
        
        # If pa != pb, we connect pa with pb
        # Before:  a -> pa   b -> pb
        #  After:  a -> pa -> pb
        #                 b --^
        # pa / pb = (b / pb) / (a / pa) * (a / b)
        #         = b_r / a_r * (a / b)
        for i, eq in enumerate(equations):
            a, b = eq
            pa, a_r, pb, b_r = *find(a), *find(b)
            if pa != pb:
                uf[pa] = (pb, b_r / a_r * values[i])
                
        res = []  
        for a, b in queries:
            if a not in uf or b not in uf:
                res.append(-1.0)
            else:
                pa, a_r, pb, b_r = *find(a), *find(b)
                if pa == pb:
                    res.append(a_r / b_r)
                else:
                    res.append(-1.0)
        return res
        