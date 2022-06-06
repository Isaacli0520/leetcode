"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Make a copy of every node and connect it to the next of its original node
        # 7 -> 13 -> 11 
        # TO
        # 7 -> 7 -> 13 -> 13 -> 11 -> 11
        curr = head
        while curr:
            new_curr = Node(curr.val, curr.next, curr.random)
            curr.next = new_curr
            curr = curr.next.next
            
        # Connect the random of each copied node to the right copied node
        curr = head
        while curr:
            if curr.next.random:
                curr.next.random = curr.next.random.next
            curr = curr.next.next
            
        # Restore the original linked list and extract the copied linked list
        curr = head
        new_head = head.next
        new_curr = new_head
        while curr:
            org_next = new_curr.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            curr.next = org_next
            curr = curr.next
            new_curr = new_curr.next
        return new_head
    
    # Hashmap
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        new_head = Node(0)
        curr = head
        prev = new_head
        while curr:
            new_curr = Node(curr.val, random=curr.random)
            d[curr] = new_curr
            if prev:
                prev.next = new_curr
            prev = new_curr
            curr = curr.next
            
        new_curr = new_head.next
        while new_curr:
            if new_curr.random:
                new_curr.random = d[new_curr.random]
            new_curr = new_curr.next
        return new_head.next
                
            
            
                