# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ret = float('-inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.oneSideMax(root)
        return self.ret

    def oneSideMax(self, root):
        if not root:
            return 0
        # Post-order traversal
        left = max(0, self.oneSideMax(root.left))
        right = max(0, self.oneSideMax(root.right))
        # Updates Max if choose both sides
        self.ret = max(self.ret, left + right + root.val)
        # Return the Max of choosing one side because once you go down a path
        # You can not go up again
        # And previous line takes care of the case of choosing both sides
        return max(left, right) + root.val