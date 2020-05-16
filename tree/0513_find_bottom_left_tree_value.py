# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findBottomLeftValue(self, root: TreeNode) -> int:
    #     level = [root]
    #     while level:
    #         last = [node.val for node in level]
    #         pairs = [(node.left, node.right) for node in level]
    #         level = [leaf for pair in pairs for leaf in pair if leaf]
    #     return last[0]
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        # Right to left BFS
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        # Leftmost node will be the last visited node
        return node.val