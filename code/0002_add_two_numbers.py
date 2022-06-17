# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        node = head
        carry = 0
        while l1 or l2 or carry:
            curr = carry
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
                
            carry = curr // 10
            curr = curr % 10
            node.next = ListNode(curr)
            node = node.next
        return head.next
        
        