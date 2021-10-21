# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Dfs + Stack
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
        return res
    
    # Recursion
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, value):
            res = 0
            if not node.left and not node.right:
                return value
            if node.left:
                res += helper(node.left, value * 10 + node.left.val)
            if node.right:
                res += helper(node.right, value * 10 + node.right.val)
            return res
        if not root:
            return 0
        return helper(root, root.val)