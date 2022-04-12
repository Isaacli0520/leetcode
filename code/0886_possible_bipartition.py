class Solution:
    # undirected graph because if a dislikes b, while b likes a, they
    # can't be put in the same group.
    # DFS
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        def helper(node):
            for nxt in graph[node]:
                if visited[nxt] == 0:
                    visited[nxt] = -visited[node]
                    if not helper(nxt):
                        return False
                else:
                    if visited[nxt] == visited[node]:
                        return False
            return True
        
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                if not helper(i):
                    return False
        return True
    
    # BFS
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        for i in range(n):
            if not visited[i]:
                stack = deque([i])
                visited[i] = 1
                while stack:
                    curr = stack.popleft()
                    for nxt in graph[curr]:
                        if not visited[nxt]:
                            visited[nxt] = -visited[curr]
                            stack.append(nxt)
                        else:
                            if visited[curr] == visited[nxt]:
                                return False
        return True
            
        