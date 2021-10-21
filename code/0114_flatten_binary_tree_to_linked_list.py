# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        # self.prev should be the root of left subtree
        # connect root of left subtree to root->right
        
        root.right = self.prev
        root.left = None
        self.prev = root

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
                