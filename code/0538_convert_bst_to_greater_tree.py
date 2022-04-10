# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot = 0
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            tot += curr.val
            curr.val = tot
            curr = curr.left
        return root
        
    # Recursive
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tot = 0
        self.helper(root)
        return root
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.right)
        self.tot += node.val
        node.val = self.tot
        self.helper(node.left)