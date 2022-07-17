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
    # BFS
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root])
        while q:
            prev = None
            for i in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left or not root.right:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root