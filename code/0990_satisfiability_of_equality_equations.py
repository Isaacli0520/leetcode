class Solution:
    # Union Find
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = {i:i for i in string.ascii_lowercase}
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
                
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)