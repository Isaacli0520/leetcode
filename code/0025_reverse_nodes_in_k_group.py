# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # If less than k nodes left, return head
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next
        
        # Reverse first k nodes
        curr = head
        prev = None
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        head.next = self.reverseKGroup(curr, k)
        return prev