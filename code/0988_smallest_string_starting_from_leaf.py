# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(nlogn) 
    #   For a perfectly balanced tree, there are (n + 1)/2 leaves and time to compare and
    #   reverse every string is O(logN), so time complexity is O(nlogn)
    # Space: O(n) (worst case: unbalanced tree that looks like a linked list)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        maxi = None
        
        def helper(path, node):
            nonlocal maxi
            if not node:
                return
            
            path.append(chr(node.val + 97))
            if not node.left and not node.right:
                tmp_s = "".join(path[::-1])
                if maxi is None or tmp_s < maxi:
                    maxi = tmp_s
                    
            helper(path, node.left)
            helper(path, node.right)
            path.pop()
            
        helper([], root)
        return maxi
        