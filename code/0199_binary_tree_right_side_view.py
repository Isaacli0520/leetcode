# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive right-side-first O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
        
        helper(root, 0)
        return res