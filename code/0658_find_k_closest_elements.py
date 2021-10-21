class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        # Find starting index
        while left < right:
            mid = left + (right - left) // 2
            # Go Right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            # Go Left
            else:
                right = mid
        return arr[left:left + k]
        