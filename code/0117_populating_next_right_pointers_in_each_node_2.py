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
    # Iterative O(1) Space
    def connect(self, root: 'Node') -> 'Node':
        node = root
        child = Node()
        level_start = child
        while node:
            # connect children
            if node.left:
                child.next = node.left
                child = child.next
            if node.right:
                child.next = node.right
                child = child.next
                
            # move parent
            node = node.next
            # If parent reaches None, go to next level
            if not node:
                node = level_start.next
                child = level_start
                level_start.next = None
        return root          
            
    
    # BFS
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        level = deque([root])
        while level:
            prev = None
            curr_level_len = len(level)
            for i in range(curr_level_len):
                curr = level.popleft()
                if prev:
                    prev.next = curr
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
                prev = curr
        return root