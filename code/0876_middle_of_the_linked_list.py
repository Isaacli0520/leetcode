# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast.next is not None:
            slow = slow.next
        return slow