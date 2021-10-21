# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Preorder Traversal
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def helper(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        return " ".join(res)
        
    # Preorder Traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(' '))
        def helper():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node
        return helper()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))