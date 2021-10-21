# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return None
    #     mid = len(nums) // 2
    #     return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, start, end):
            if start == end:
                return None
            mid = start + (end - start) // 2
            left = helper(nums, start, mid)
            right = helper(nums, mid  + 1, end)
            return TreeNode(nums[mid], left, right)
        return helper(nums, 0, len(nums))