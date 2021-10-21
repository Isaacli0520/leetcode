# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(node, left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            return helper(node.left, True) + helper(node.right, False)
        return helper(root, False)
    
    # Iterative
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = []
        tot = 0
        while root or stack:
            c = 0
            while root:
                c += 1
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.left and not root.right and c > 1:
                tot += root.val
            root = root.right
        return tot