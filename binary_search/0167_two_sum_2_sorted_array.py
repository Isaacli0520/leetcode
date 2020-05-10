class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        history = []
        for i in range(l):
            if nums[i] not in history:
                history.append(nums[i])
                lo, hi = i + 1, l - 1
                tmp_t = target - nums[i]
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    if nums[mid] == tmp_t:
                        return [i + 1, mid + 1]
                    elif nums[mid] < tmp_t:
                        lo = mid + 1
                    elif nums[mid] > tmp_t:
                        hi = mid - 1
        return [-1, -1]