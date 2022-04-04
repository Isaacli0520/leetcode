# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two pointers
    # Move p1 n times (n + 1 times if p1 starts at dummy)
    # Move p1 and p2 together until p1 is None, then p2
    # has moved tot_len - n times, therefore is at nth node 
    # from end of list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1, p2 = dummy, dummy
        for i in range(n + 1):
            p1 = p1.next
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next