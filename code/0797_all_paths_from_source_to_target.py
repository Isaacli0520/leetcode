class Solution:
    # DFS
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, stack = [], [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == len(graph) - 1:
                res.append(path)
            for nxt in graph[node]:
                stack.append((nxt, path + [nxt]))
        return res
        
    # Backtracking
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def helper(path, node):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            for nxt in graph[node]:
                path.append(nxt)
                helper(path, nxt)
                path.pop()
                
        helper([0], 0)
        return res
    
    # Backtracking
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        res = []
        def helper(node):
            path.append(node)
            if node ==  len(graph) - 1:
                res.append([i for i in path])
                path.pop()
                return
            for nxt in graph[node]:
                helper(nxt)
            path.pop()
        helper(0)
        return res