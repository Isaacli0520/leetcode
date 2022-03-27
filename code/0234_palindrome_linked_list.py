# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev, tmp = None, None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        if fast:
            slow = slow.next
        while prev is not None:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
        