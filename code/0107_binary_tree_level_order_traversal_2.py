# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack, res, level = [[root]], [], [root]
        while level:
            pairs = [(node.left, node.right) for node in level]
            level = [leaf for pair in pairs for leaf in pair if leaf]
            stack.append(level)
        stack.pop()
        while stack:
            res.append([node.val for node in stack.pop()])
        return res