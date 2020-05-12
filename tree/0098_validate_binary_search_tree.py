# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        # inorder traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val :
                return False
            pre = root
            root = root.right
        return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, mini, maxi):
            if not root:
                return True
            # check root & left & right
            return (not mini or root.val > mini.val) and (not maxi or root.val < maxi.val) and helper(root.left, mini, root) and helper(root.right, root, maxi)
        return helper(root, None, None)