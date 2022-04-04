# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, p1: Optional[ListNode], p2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
            else:
                curr.next = p1
                p1 = p1.next
            curr = curr.next
        if p1 is not None:
            curr.next = p1
        if p2 is not None:
            curr.next = p2
        return head.next