class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            count = 0
            j = n - 1
            # count numbers smaller than mid
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1;
                count += j + 1
            if count < k:
                # will find the Kth smallest element in the matrix
                left = mid + 1
            else:
                # when count == k, this will set right to mid
                # and let left approach the Kth smallest element
                # step by step
                right = mid
        return left