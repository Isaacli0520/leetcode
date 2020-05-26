class Solution:
    # Three States
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = [0] * numCourses
        d = collections.defaultdict(list)
        for c, prereq in prerequisites:
            d[prereq].append(c)
            
        # three states
        #   0 not processed
        #  -1 processing
        #   1 processed
        def dfs(course):
            # If processed return
            if states[course] == 1:
                return False
            # Still processing, cycle found
            if states[course] == -1:
                return True
            # Set as processing
            states[course] = -1
            for cand in d[course]:
                if dfs(cand):
                    return True
            # Set as processed
            states[course] = 1
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
    
    # Use stack to track state (slower)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for c, prereq in prerequisites:
            d[prereq].append(c)
        visited = []
        
        def dfs(course, stack):
            if course in visited:
                return False
            if course in stack:
                return True
            
            stack.append(course)
            
            for cand in d[course]:
                if dfs(cand, stack):
                    return True
            visited.append(course)
            stack.pop()
            return False
        
        for i in range(numCourses):
            if dfs(i, []):
                return False
        return True