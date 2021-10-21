# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            pairs = [(node.left, node.right) for node in level]
            # next level = children of this level
            level = [leaf for pair in pairs for leaf in pair if leaf]
        return res