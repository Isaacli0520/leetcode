from collections import deque
class Solution:
    # Sort nums2, for biggest num, choose nums1's biggest
    # if it's greater, else pick the smallest
    #
    # Two pointers or deque
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_s = sorted([(i, num) for i, num in enumerate(nums2)], key=lambda x:x[1], reverse=True)
        nums1_s = deque(sorted(nums1))
        
        res = [0] * len(nums2)
        for i, num in nums2_s:
            if num < nums1_s[-1]:
                res[i] = nums1_s.pop()
            else:
                res[i] = nums1_s.popleft()
        return res
        