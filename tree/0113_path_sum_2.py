# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, sum, [root.val])]
        res = []
        while stack:
            node, tmp_sum, trace = stack.pop()
            if not node.left and not node.right and node.val == tmp_sum:
                res.append(trace)
            if node.left:
                stack.append((node.left, tmp_sum - node.val, trace + [node.left.val]))
            if node.right:
                stack.append((node.right, tmp_sum - node.val, trace + [node.right.val]))
        return res