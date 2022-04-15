# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        d = [self.minDepth(root.left), self.minDepth(root.right)]
        # min of left right depth if min depth not 0, else max depth
        return 1 + (min(d) or max(d))
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left is None and curr.right is None:
                    return depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack, level = [], [root]
        d = 1
        while level:
            pairs = [(node.left, node.right) for node in level]
            level = []
            for pair in pairs:
                if pair[0]:
                    level.append(pair[0])
                if pair[1]:
                    level.append(pair[1])
                if not pair[0] and not pair[1]:
                    return d
            d += 1