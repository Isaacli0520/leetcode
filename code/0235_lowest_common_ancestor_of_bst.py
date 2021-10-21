# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        next = None
        if p.val < root.val > q.val:
            next = root.left
        elif p.val > root.val < q.val:
            next = root.right
        if next:
            return self.lowestCommonAncestor(next, p, q)
        else:
            return root