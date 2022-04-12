# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_height(node):
            if not node:
                return 0
            return 1 + get_height(node.left)
        
        lh = get_height(root.left)
        rh = get_height(root.right)
        if lh == rh:
            return self.countNodes(root.right) + pow(2, lh)
        else:
            return self.countNodes(root.left) + pow(2, rh)
            