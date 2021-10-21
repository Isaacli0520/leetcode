class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r, c = len(triangle), len(triangle[-1])
        row = [triangle[-1][i] for i in range(c)]
        for i in range(r - 2, -1, -1):
            for j in range(i + 1):
                row[j] = triangle[i][j] + min(row[j], row[j + 1])
        return row[0]