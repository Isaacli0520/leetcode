# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        if not root:
            return True
        return helper(root.left, root.right)
    
    # Iterative
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if (left and not right) or (right and not left) or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True