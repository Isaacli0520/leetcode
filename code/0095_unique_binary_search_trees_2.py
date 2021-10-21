# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # generate a tree with values from first to last
        def generate(first, last):
            res = []
            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        res.append(TreeNode(root, left, right))
            return res or [None]
        if n == 0: return []
        return generate(1, n)
                