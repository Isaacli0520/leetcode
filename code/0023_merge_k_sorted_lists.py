# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Heap
    # Time: O(Nlogk), N: total number of Nodes; k: number of linked lists
    #       (O(logk) for pop and push into heap)
    # Space: O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        head = ListNode()
        curr = head
        pk = 0
        for node in lists:
            if node:
                heapq.heappush(hp, (node.val, pk, node))
                pk += 1
        while hp:
            _val, _pk, node = heapq.heappop(hp)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(hp, (node.val, pk, node))
                pk += 1
        return head.next
            
            
    # Divide and Conquer
    # Time: O(Nlogk), N: total number of nodes; k number of linked lists
    # Space: O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeLists(left, right)
        
    
    def mergeLists(self, a, b):
        head = ListNode()
        curr = head
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        if a:
            curr.next = a
        if b:
            curr.next = b
        return head.next
        
        
        