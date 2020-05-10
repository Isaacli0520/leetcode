# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_d = self.getDepth(root.left)
        right_d = self.getDepth(root.right)
        if left_d == right_d:
            return pow(2, left_d) + self.countNodes(root.right)
        else:
            return pow(2, right_d) + self.countNodes(root.left)
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
    
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    