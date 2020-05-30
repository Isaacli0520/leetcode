class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        r, c = len(M), len(M[0])
        visited = [0 for i in range(r)]
        def dfs(i):   
            # For a students, visit all his/her friends
            visited[i] = 1
            for j in range(r):
                if not visited[j] and M[i][j]:
                    dfs(j)
        count = 0
        # Only need to iterate through each row if the student
        # is not yet visited
        for i in range(r):
            if not visited[i]:
                count += 1
                dfs(i)
                    
        return count