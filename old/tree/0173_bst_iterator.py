# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = collections.deque()
        self.root = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        tmp = self.stack.pop()
        self.root = tmp.right
        return tmp.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.root or self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()