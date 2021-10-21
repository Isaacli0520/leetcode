# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        level = [root]
        res = []
        while any(level):
            res.append(max([node.val for node in level]))
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res