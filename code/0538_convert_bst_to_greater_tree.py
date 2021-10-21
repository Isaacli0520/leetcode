# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def __init__(self):
        self.so_far = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        root.val += self.so_far
        self.so_far = root.val
        self.convertBST(root.left)
        return root
    
    # DFS
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = []
        so_far = 0
        ret = root
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            root.val += so_far
            so_far = root.val
            root = root.left
        return ret