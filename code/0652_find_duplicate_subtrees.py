# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    # Preorder and Postorder serialization work but not inorder
    # because inorder can give same serialization for symmetric trees
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = collections.defaultdict(int)
        res = []
        
        def helper(node):
            if not node:
                return "#"
            tmp = ",".join([str(node.val), helper(node.left),helper(node.right)])
            if tmp in d and d[tmp] == 1:
                res.append(node)
            d[tmp] += 1
            return tmp
        
        helper(root)
        return res
            