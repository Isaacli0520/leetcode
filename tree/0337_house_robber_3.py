# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            
            left = helper(node.left)
            
            right = helper(node.right)
            
            # if rob now, can only rob later of left and right child
            now = node.val + left[1] + right[1]
            # if rob later, can rob now and later of left and right child
            later = max(left) + max(right)
            
            return (now, later)
        return max(helper(root))