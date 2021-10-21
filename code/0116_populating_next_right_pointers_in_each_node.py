"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # Iterative
    def connect(self, root: 'Node') -> 'Node':
        # level by level from left
        ret = root
        while root and root.left:
            next = root.left
            while root:
                # connect root.left to root.right
                root.left.next = root.right
                # connect root.right to root.next.left if root.next exists
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None
                root = root.next
            # go to the next level
            root = next
        return ret
    
    # Recursive
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if not root.left and not root.right:
            if not root.next:
                root.next = None
                return root
            else:
                return
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
        return root