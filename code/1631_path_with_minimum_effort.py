class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        
        heap = [(0, (0, 0))]
        heapq.heapify(heap)
        dist = {}
        while heap:
            effort, coord = heapq.heappop(heap)
            if coord == (r - 1, c - 1):
                return effort
            if coord not in dist:
                dist[coord] = effort
                i, j = coord
                for m, n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= m and m < r and 0 <= n and n < c:
                        heapq.heappush(heap, (max(abs(heights[i][j] - heights[m][n]), effort), (m, n)))
        
        return dist[(r - 1, c - 1)]