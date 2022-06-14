class Solution:
    # BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        prereqs = [0] * numCourses
        for c, prereq in prerequisites:
            graph[prereq].append(c)
            prereqs[c] += 1
        
        res = []
        queue = deque(i for i in range(numCourses) if prereqs[i] == 0)
        while queue:
            c = queue.popleft()
            res.append(c)
            for nxt in graph[c]:
                prereqs[nxt] -= 1
                if prereqs[nxt] == 0:
                    queue.append(nxt)
        return res if sum(prereqs) == 0 else []
        
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