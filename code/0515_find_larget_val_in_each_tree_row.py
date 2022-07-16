# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            maxi = None
            for i in range(len(q)):
                node = q.popleft()
                if maxi is None:
                    maxi = node.val
                else:
                    maxi = max(maxi, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxi)
        return res

    def largestValues(self, root: TreeNode) -> List[int]:
        level = [root]
        res = []
        while any(level):
            res.append(max([node.val for node in level]))
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res