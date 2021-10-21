# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = postorder.pop()
        idx = inorder.index(root)
        right = self.buildTree(inorder[idx + 1:], postorder)
        left = self.buildTree(inorder[:idx], postorder)
        return TreeNode(root, left, right)