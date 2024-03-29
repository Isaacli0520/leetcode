# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and curr.val <= prev.val:
                return False
            prev = curr
            curr = curr.right
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        
        def helper(node):
            if not node:
                return True
            
            nonlocal prev
            if not helper(node.left):
                return False
            if prev and prev.val >= node.val:
                return False
            prev = node
            if not helper(node.right):
                return False
            return True
        
        return helper(root)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, mini, maxi):
            if not node:
                return True
            if mini and node.val <= mini.val:
                return False
            if maxi and node.val >= maxi.val:
                return False
            
            return helper(node.left, mini, node) and helper(node.right, node, maxi)
        return helper(root, None, None)
        
            
            