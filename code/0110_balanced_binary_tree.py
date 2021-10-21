# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # return -1 if not height-balanced
        # end early if either left or right is unbalanced
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return helper(root) != -1