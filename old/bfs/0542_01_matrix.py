class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        ret = [[0 for j in range(c)] for i in range(r)]
        stack = collections.deque()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    ret[i][j] = r + c + 1
                else:
                    stack.append((i, j))
        # BFS
        # For every visited (distance determined) node
        # find the distance of its neighbors
        # For example, with all 0s on the stack
        # Every neighbor that is not 0 should be updated with 1 because
        # 1 is the closest distance to a 0
        # After all 0s are processed, we process all 1s
        # And we build up the matrix from 0, 1 ... to the longest distance
        # 
        # Intuition:
        # For distance n to exist, distance n - 1 must exist as its neighbor
        # (otherwise it's a 0 not a 1 and distance is 1) Therefore we build
        # the matrix with bfs
        while stack:
            i, j = stack.popleft()
            tmp = ret[i][j] + 1
            for m, n in [(i - 1, j),(i, j - 1),(i + 1,j),(i, j + 1)]:
                if 0 <= m < r and 0 <= n < c and ret[m][n] > tmp:
                    ret[m][n] = tmp
                    stack.append((m, n))
        return ret