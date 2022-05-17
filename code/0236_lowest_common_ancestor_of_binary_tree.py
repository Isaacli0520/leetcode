# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if not node:
                return None
            if node == p or node == q:
                return node

            left = helper(node.left)
            right = helper(node.right)
            
            # Since p and q are unique, if they are found in left and right
            # the lowest common ancestor must be current root
            if left and right:
                return node
            # They must be on one side
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return helper(root)