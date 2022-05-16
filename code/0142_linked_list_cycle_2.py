# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #          (k - m)   m    k
    # --------> cycle ------> meet
    #             ---------->   | 
    #             |             |     <- Fast pointer travels 2k, so from meet
    #             ----------<----        to meet, the length is k
    #                  (k - m)           From meet to cycle, the length is k - m
    # 
    # After fast and slow meet for the first time, move slow
    # to the head again, and let fast and slow go at same speed
    # When they meet again, it will be at the cycle node.
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        is_cycle = False
        # Find if there is cycle, and if there is, stop at 
        # where fast and slow meet
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                is_cycle = True
                break
        if not is_cycle:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
        