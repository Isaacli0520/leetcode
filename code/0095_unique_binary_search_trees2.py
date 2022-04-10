# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # [start, end)
        def helper(start, end):
            if start >= end:
                return [None]
                
            res = []
            for i in range(start, end):
                for l in helper(start, i):
                    for r in helper(i + 1, end):
                        res.append(TreeNode(i + 1, l, r))
            return res
        
        return helper(0, n)