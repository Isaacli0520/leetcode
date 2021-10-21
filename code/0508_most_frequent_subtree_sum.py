# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def helper(node):
            if not node:
                return 0
            s = node.val + helper(node.left) + helper(node.right)
            count[s] += 1
            return s
        
        count = collections.Counter()
        helper(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]