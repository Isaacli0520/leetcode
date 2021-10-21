# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Recursive
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     left = self.postorderTraversal(root.left)
    #     right = self.postorderTraversal(root.right)
    #     return left + right + [root.val]
    
    # Iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = collections.deque()
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                res.appendleft(node.val)
        return res