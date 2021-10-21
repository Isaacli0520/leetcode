# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Dfs
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        prev = None
        mini = float('inf')
        # Inorder Traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and abs(root.val - prev.val) < mini:
                mini = abs(root.val - prev.val)
            prev = root
            root = root.right
        return mini
    
    # Recursive No Global
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node, prev, mini):
            if not node:
                return prev, mini
            prev, mini = inorder(node.left, prev, mini)
            if prev:
                mini = min(mini, abs(node.val - prev.val))
            return inorder(node.right, node, mini)
        return inorder(root, None, float('inf'))[1]
        