class Solution:
    # Union Find
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = {i + 1:i + 1 for i in range(len(edges))}
            
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        for edge in edges:
            u, v = find(edge[0]), find(edge[1])
            if u == v:
                return edge
            uf[u] = v
        
        
            
            