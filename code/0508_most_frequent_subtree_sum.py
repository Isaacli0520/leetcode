# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        d = collections.defaultdict(int)
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            
            cur_sum = left + right + node.val
            d[cur_sum] += 1
            return cur_sum
        
        helper(root)
        maxi = max(d.values())
        return [k for k, v in d.items() if v == maxi]