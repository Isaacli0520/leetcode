# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Max Diameter of a node = max_depth(left) + max_depth(right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        self.max_depth(root)
        return self.max_len
    
    def max_depth(self, node):
        if node is None:
            return 0
        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        self.max_len = max(self.max_len, left + right)
        return 1 + max(left, right)