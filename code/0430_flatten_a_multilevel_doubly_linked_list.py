"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # Iterative
    """
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # Iterative DFS
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        stack = []
        while curr:
            # Connect current to child
            if curr.child:
                # Save current's next if it's not None
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            elif curr.next is None:
                # Connect to previous next if there is any
                if stack:
                    prev_next = stack.pop()
                    curr.next = prev_next
                    prev_next.prev = curr
            curr = curr.next
        return head

    # Iterative Stack DFS
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        stack = [head]
        prev = None
        while stack:
            curr = stack.pop()
            curr.prev = prev
            if prev:
                prev.next = curr
            prev = curr
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        return head
    
    # Recursion
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(curr):
            tail = curr
            while curr:
                tmp_next = curr.next
                tail = curr
                if curr.child:
                    c_tail = helper(curr.child)
                    curr.next = curr.child
                    curr.child.prev = curr
                    if tmp_next:
                        c_tail.next = tmp_next
                        tmp_next.prev = c_tail
                    else:
                        # Corner case:
                        # 6 -> 7 -> 8 -> null
                        # 2 -> 3 -> null
                        # null 4 -> 5 -> null
                        # Then the tail of the second level is 5
                        # instead of 3
                        tail = c_tail
                    curr.child = None
                curr = tmp_next
            return tail
            
        helper(head)
        
        return head