# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #  Preorder: [#root] [#left_root left] [#right_root right]
    # Postorder: [left #left_root] [right #right_root] [#root]
    #
    # Q: Why could there be more than one answer?
    # A: Because maybe the value next to #root in preorder is #right_root,
    #    (the tree may not have a left subtree)
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        left_root = preorder[1]
        left_root_idx = postorder.index(left_root)
        
        root.left = self.constructFromPrePost(preorder[1:left_root_idx + 2], postorder[:left_root_idx + 1])
        root.right = self.constructFromPrePost(preorder[left_root_idx + 2:], postorder[left_root_idx + 1:])
        
        return root