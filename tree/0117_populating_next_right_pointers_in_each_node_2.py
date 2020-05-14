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
    def connect(self, root: 'Node') -> 'Node':
        ret = root
        node = root
        level = child = Node()
        while node:
            # connect to node.left, if node.left, 
            # connect and move to next(node.left)
            # also sets the starting node of next level(level.next)
            child.next = node.left
            if child.next:
                child = child.next
            # connect to node.right, if node.right
            # connect and move to next(node.right)
            # also sets the starting node of next level(level.next)
            child.next = node.right
            if child.next:
                child = child.next
            # move to next parent node
            node = node.next
            if not node:
                # end of level, go to next level(node = level.next)
                node = level.next
                # clear child
                child = level
        return ret