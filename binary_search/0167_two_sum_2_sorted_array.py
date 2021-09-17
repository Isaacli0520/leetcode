class Solution:
    # Two Pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1
        
    # # Binary Search
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     n = len(numbers)
    #     visited = []
    #     for i in range(n):
    #         if numbers[i] not in visited:
    #             visited.append(numbers[i])
    #             tmp = target - numbers[i]
    #             left, right = i + 1, n - 1
    #             while left <= right:
    #                 mid = int(left + (right - left) / 2)
    #                 if numbers[mid] == tmp:
    #                     return [i + 1, mid + 1] # 1-indexed not 0-indexed
    #                 elif numbers[mid] > tmp:
    #                     right = mid - 1
    #                 elif numbers[mid] < tmp:
    #                     left = mid + 1
    #     return [-1, -1]