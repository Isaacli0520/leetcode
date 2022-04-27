class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        end = points[0][1]
        cnt = 1
        for point in points:
            if point[0] > end:
                end = point[1]
                cnt += 1
        return cnt