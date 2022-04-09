# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node, res):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            helper(node.left, res)
            helper(node.right, res)
        tmp = []
        helper(root, tmp)
        return ",".join(tmp)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split(","))
        def helper2(ls):
            val = next(data)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = helper2(ls)
            node.right = helper2(ls)
            return node
        return helper2(data)
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))