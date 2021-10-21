# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []
    
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack, res = [], []
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         tmp = stack.pop()
    #         res.append(tmp.val)
    #         root = tmp.right
    #     return res