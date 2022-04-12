import collections
class Solution:
    # BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Count the num of prereq courses of each course
        d = collections.defaultdict(list)
        prereq_count_ls = [0] * numCourses
        for c, prereq in prerequisites:
            d[prereq].append(c)
            prereq_count_ls[c] += 1
            
        # Go through all courses that has no prereqs, append
        # further no prereq courses as courses are taken
        bfs = collections.deque(i for i in range(numCourses) if prereq_count_ls[i] == 0)
        while bfs:
            course = bfs.popleft()
            for next_course in d[course]:
                prereq_count_ls[next_course] -= 1
                if prereq_count_ls[next_course] == 0:
                    bfs.append(next_course)
                    
        # In the end, all courses should have no prereqs
        return not sum(prereq_count_ls)

    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for c, prereq in prerequisites:
            graph[prereq].append(c)
        onPath = [False] * numCourses
        visited = [False] * numCourses
        hasCycle = False
        def helper(curr):
            nonlocal hasCycle
            if onPath[curr]:
                hasCycle = True
                return
            if visited[curr] or hasCycle:
                return
            visited[curr] = True
            onPath[curr] = True
            for course in graph[curr]:
                helper(course)
            onPath[curr] = False
            
        for i in range(numCourses):
            helper(i)
        return not hasCycle

    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for c, prereq in prerequisites:
            d[prereq].append(c)
            
        # Store the states of every course
        # -1 means taking this course, if there is a cycle, doing a dfs from this
        #    node can go back to this node, therefore finding the cycle
        # 1 means this course can be taken without a cycle
        # 0 means unvisited courses
        states = [0] * numCourses
        
        def dfs(c):
            # We found a cycle, return True
            if states[c] == -1:
                return True
            # The course is processed, no cycle, return False
            if states[c] == 1:
                return False
            
            # Mark this as -1 and do dfs, see if there is any cycle
            states[c] = -1
            for next_c in d[c]:
                if dfs(next_c):
                    return True
            
            # No cycle, mark this course as processed
            states[c] = 1
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True