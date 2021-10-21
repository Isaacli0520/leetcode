# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, level = [], [root]
        i = 1
        while level:
            res.append([node.val for node in level])
            if i % 2 == 0:
                # left to right
                pairs = [(level[j].left, level[j].right) for j in range(len(level) - 1, -1, -1)]
            else:   
                # right to left
                pairs = [(level[j].right, level[j].left) for j in range(len(level) - 1, -1, -1)]
            level = [leaf for pair in pairs for leaf in pair if leaf]
            i += 1
        return res
                