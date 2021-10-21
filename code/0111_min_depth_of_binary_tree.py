# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        d = [self.minDepth(root.left), self.minDepth(root.right)]
        # min of left right depth if min depth not 0, else max depth
        return 1 + (min(d) or max(d))
    
        # if not root:
        #     return 0
        # stack, level = [], [root]
        # d = 1
        # while level:
        #     pairs = [(node.left, node.right) for node in level]
        #     level = []
        #     for pair in pairs:
        #         if pair[0]:
        #             level.append(pair[0])
        #         if pair[1]:
        #             level.append(pair[1])
        #         if not pair[0] and not pair[1]:
        #             return d
        #     d += 1