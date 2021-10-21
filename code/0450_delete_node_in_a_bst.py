# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If no left child, return right child for root to connect to
            if not root.left:
                return root.right
            
            # If left child, find max of left subtree and replace root with it
            curr = root.left
            while curr.right:
                curr = curr.right
            root.val = curr.val
            # Delete the child from left subtree b/c it's already the root
            root.left = self.deleteNode(root.left, curr.val)
        return root