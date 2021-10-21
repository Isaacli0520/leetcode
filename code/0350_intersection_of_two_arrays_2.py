class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a == b:
                res.append(a)
                i += 1
                j += 1
            elif b > a:
                i += 1
            else:
                j += 1
                    
        return res