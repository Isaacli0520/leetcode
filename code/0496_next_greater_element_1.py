class Solution:
    # Increasing monotonic stack
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        
        return [d.get(num, -1) for num in nums1]

    # Decreasing monotonic stack
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                res[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        return [res.get(num, -1) for num in nums1]
            