# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #   inorder = [9],  [3],   [15,   20,   7]
    #            left |  root  |    right
    # postorder = [9]   [15,   7,   20],   [3]
    #            left |     right   |  root 
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        val = postorder[-1]
        idx = inorder.index(val)
        
        root = TreeNode(val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root