# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(node):
            if node:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return " ".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        vals = collections.deque([int(s) for s in data.split(" ")])
        def build(mini, maxi):
            if vals and mini < vals[0] < maxi:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(mini, val)
                node.right = build(val, maxi)
                return node
            else:
                return None
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))