# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Level by level O(n)
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        level = [root]
        while level:
            res.append(level[-1].val)
            pairs = [(node.left, node.right) for node in level]
            level = [leaf for pair in pairs for leaf in pair if leaf]
        return res
            
    # Recursive right-side-first O(n)
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(node, depth):
            if node:
                # First occurance of new level
                if len(res) == depth:
                    res.append(node.val)
                # Right side first
                helper(node.right, depth + 1)
                helper(node.left, depth + 1)
        res = []
        helper(root, 0)
        return res