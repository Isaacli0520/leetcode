# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(node):
            if not node.left and not node.right: return [str(node.val)]
            res = []
            if node.left:
                res += [str(node.val) + "->" + l for l in helper(node.left)]
            if node.right:
                res += [str(node.val) + "->" + r for r in helper(node.right)]
            return res
        if not root:
            return []
        return helper(root)
    
    # Recursion with global variable
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        
        def helper(node, s):
            if not node.left and not node.right:
                self.res.append(s)
            if node.left:
                helper(node.left, s + "->" + str(node.left.val))
            if node.right:
                helper(node.right, s + "->" + str(node.right.val))
                
        if not root:
            return []
        helper(root, str(root.val))
        return self.res
    
    # Dfs
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right:
                res.append(s)
            if node.left:
                stack.append((node.left, s + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, s + "->" + str(node.right.val)))
        return res
            



