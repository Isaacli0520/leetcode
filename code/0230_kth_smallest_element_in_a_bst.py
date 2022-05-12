# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        def helper(node):
            nonlocal res
            nonlocal k
            if not node or k <= 0:
                return
            helper(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            helper(node.right)
        helper(root)
        return res

    # Iterative
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right