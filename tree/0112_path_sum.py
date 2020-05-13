# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root and root.val == sum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    
    # DFS
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = [(root, sum)]
        while stack:
            node, tmp_sum  = stack.pop()
            if node:
                if not node.left and not node.right and node.val == tmp_sum:
                    return True
                stack.append((node.left, tmp_sum - node.val))
                stack.append((node.right, tmp_sum - node.val))
        return False
            