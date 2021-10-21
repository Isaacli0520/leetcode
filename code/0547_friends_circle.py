class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # For each city, find all connected city and mark them as visited
        
        n = len(isConnected)
        visited = [0] * n
        def dfs(i):
            visited[i] = 1
            for j in range(n):
                if not visited[j] and isConnected[i][j]:
                    dfs(j)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count