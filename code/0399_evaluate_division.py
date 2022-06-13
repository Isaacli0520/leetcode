class Solution:
    # BFS
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        def find_query(a, b):
            if a not in graph or b not in graph:
                return -1
            
            queue = deque([(a, 1)])
            visited = set()
            while queue:
                node, curr = queue.popleft()
                if node == b:
                    return curr
                visited.add(node)
                for nxt, weight_nxt in graph[node]:  
                    if nxt not in visited:
                        queue.append((nxt, curr * weight_nxt))
            return -1
        
        return [find_query(a, b) for a, b in queries]
    
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
        