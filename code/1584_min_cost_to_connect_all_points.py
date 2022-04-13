class Solution:
    # Kruskal's Algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Sort all distances
        dists = []
        for a in range(len(points)):
            for b in range(a, len(points)):
                i, j, m, n = *points[a], *points[b]
                dists.append((i, j, m, n, abs(i - m) + abs(j - n)))
        dists = sorted(dists, key=lambda x:x[-1])
        
        uf = {}
        
        def find(x):
            uf[x] = uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
                
        cnt = len(points)
        tot = 0
        for i, j, m, n, d in dists:
            # Break early if we have connected all points
            if cnt == 1:
                break
            a, b = find((i, j)), find((m, n))
            if a != b:
                uf[a] = b
                cnt -= 1
                tot += d
        return tot