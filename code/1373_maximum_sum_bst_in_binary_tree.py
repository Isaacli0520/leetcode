# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Post order Traversal
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxi = -inf
        self.helper(root)
        return self.maxi if self.maxi > 0 else 0
        
    def helper(self, node):
        if not node:
            # Return inf and -inf to make finding the min
            # max of a node with empty left or right easier
            return True, inf, -inf, 0
        
        # Record left and right nodes' min, max, and sum
        l_bst, l_min, l_max, l_sum = self.helper(node.left)
        r_bst, r_min, r_max, r_sum = self.helper(node.right)
        if l_bst and r_bst:
            if node.val > l_max and node.val < r_min:
                new_sum = l_sum + r_sum + node.val
                self.maxi = max(self.maxi, new_sum)
                return True, min(node.val, l_min), max(node.val, r_max), new_sum
        return False, 0, 0, 0
            
            