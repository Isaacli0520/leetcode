# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Stores count of sums from root to any node
        self.cache = collections.defaultdict(int)
        self.ret = 0
        self.cache[0] = 1
        
        def helper(node, so_far):
            if not node:
                return
            so_far += node.val
            # Count the number of predecessors of current node that has 
            # root to node sum of (so_far - sum). Because from this node to
            # current node, the sum of path should be 
            # (so_far - (so_far - sum)) = sum
            self.ret += self.cache[so_far - sum]
            # Update cache for current node
            self.cache[so_far] += 1
            helper(node.left, so_far)
            helper(node.right, so_far)
            # Reset cache after use because the path must go downward
            self.cache[so_far] -= 1
            
        helper(root, 0)
        return self.ret