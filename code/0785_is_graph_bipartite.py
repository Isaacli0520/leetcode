class Solution:
    # DFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        
        def helper(node):
            for nxt in graph[node]:
                if visited[nxt] != 0:
                    if visited[nxt] == visited[node]:
                        return False
                else:
                    visited[nxt] = -visited[node]
                    if not helper(nxt):
                        return False
            return True
        
        for i in range(len(graph)):
            if visited[i] == 0:
                visited[i] = -1
                if not helper(i):
                    return False
        return True
    
    # BFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        
        for i in range(len(graph)):
            if not visited[i]:
                visited[i] = 1
                stack = deque([i])
                while stack:
                    curr = stack.popleft()
                    for nxt in graph[curr]:
                        if visited[nxt] != 0:
                            if visited[curr] == visited[nxt]:
                                return False
                        else:
                            visited[nxt] = -visited[curr]
                            stack.append(nxt)
        
        return True