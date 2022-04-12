class Solution:
    # BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for c, prereq in prerequisites:
            graph[prereq].append(c)
            indegrees[c] += 1
        
        bfs = deque([i for i in range(numCourses) if indegrees[i] == 0])
        topo_sort = [i for i in bfs]
        while bfs:
            curr = bfs.popleft()
            for course in graph[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    bfs.append(course)
                    topo_sort.append(course)
        return topo_sort if sum(indegrees) == 0 else []
        
    # DFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for c, prereq in prerequisites:
            graph[prereq].append(c)
        
        onPath = [False] * numCourses
        visited = [False] * numCourses
        hasCycle = False
        topo_sort = []
        
        def helper(node):
            nonlocal hasCycle
            if onPath[node]:
                hasCycle = True
                return
            if hasCycle or visited[node]:
                return
            onPath[node] = True
            visited[node] = True
            for course in graph[node]:
                helper(course)
            topo_sort.append(node)
            onPath[node] = False
            
        for i in range(numCourses):
            helper(i)
            
        if hasCycle:
            return []
        else:
            return topo_sort[::-1]