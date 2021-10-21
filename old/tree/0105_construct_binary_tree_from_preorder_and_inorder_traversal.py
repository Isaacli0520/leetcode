# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Without Modifying lists
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.d = {}
        # Cache
        for i, n in enumerate(inorder):
            self.d[n] = i
        return self.helper(preorder, inorder,0,len(preorder)-1,0,len(inorder)-1)
        
    def helper(self, preorder, inorder, pre_start, pre_end, in_start, in_end):   
        if pre_start <= pre_end and in_start <= in_end:
            root = preorder[pre_start]
            idx = self.d[root]
            nums_left = idx - in_start
            left = self.helper(preorder, inorder,pre_start+1, pre_start+nums_left+1,in_start,idx - 1)
            right = self.helper(preorder, inorder,pre_start+nums_left+1,pre_end,idx+1,in_end)
            tree = TreeNode(root, left, right)
            return tree
        return None

    # Modifying lists
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = preorder.pop(0)
            idx = inorder.index(root)
            left = self.buildTree(preorder, inorder[:idx])
            right = self.buildTree(preorder, inorder[idx + 1:])
            return TreeNode(root, left, right)