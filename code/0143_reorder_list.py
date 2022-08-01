# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find Middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast.next:
            slow = slow.next
        
        # Reverse second half
        curr = slow
        prev = None
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        # Connect
        left = head
        right = prev
        while left:
            left.next, left, right = right, right, left.next
        return