# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iteration
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
            
        prev2 = None
        curr = prev.next
        
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = tmp
            
        prev.next.next = curr
        prev.next = prev2
        
        return dummy.next
        
    # Recursion
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)[0]
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
        
    def reverseN(self, node, n):
        if n == 1:
            return node, node.next
        last, last_next = self.reverseN(node.next, n - 1)
        node.next.next = node
        node.next = last_next
        return last, last_next