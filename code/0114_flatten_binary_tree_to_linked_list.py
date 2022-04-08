# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        
        # if root.left is None, this subtree is already flattened
        if root.left:
            # connect rightmost node of root.left to root.right
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = root.right
            
            root.right = root.left
            root.left = None
        

    # Iterative O(n)
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            # connect rightmost node of curr.left to curr.right
            if curr.left:
                # find rightmost node of curr.left
                pre = curr.left
                while pre.right:
                    pre = pre.right
                # connect connect rightmost node of curr.left to curr.right
                pre.right = curr.right
                # connect left subtree to the right of curr
                curr.right = curr.left
                # set left of curr to None
                curr.left = None
            # move curr down
            curr = curr.right
                