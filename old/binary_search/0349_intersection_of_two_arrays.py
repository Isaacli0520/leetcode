class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            n1 = sorted(nums1)
            n2 = nums2
        else:
            n1 = sorted(nums2)
            n2 = nums1
        for x in n2:
            if x in res:
                continue
            left, right = 0, len(n1)
            while left < right:
                mid = left + (right - left) // 2
                if n1[mid] < x:
                    left = mid + 1
                elif n1[mid] > x:
                    right = mid
                else:
                    res.append(x)
                    break
        return res
            
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:   
        return list(set(nums1) & set(nums2))
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a == b:
                res.append(a)
                while i < len(nums1) and nums1[i] == a: i += 1
                while j < len(nums2) and nums2[j] == b: j += 1
            elif b > a:
                while i < len(nums1) and a == nums1[i]: i += 1
            else:
                while j < len(nums2) and b == nums2[j]: j += 1
                    
        return res