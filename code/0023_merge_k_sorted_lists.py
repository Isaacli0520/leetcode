# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Divide and conquer
    # merge log k times (k is the number of lists)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
    
    def merge(self, p1, p2):
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
                
            
        
        