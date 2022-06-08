# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        res = 1
        while queue:
            level_length = len(queue)
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for i in range(level_length):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
        return res
                