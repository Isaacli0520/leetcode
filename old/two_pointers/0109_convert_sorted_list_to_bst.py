# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        # Odd Case
        #
        # 1 2 3 4 5
        # s   f
        #   s     f
        # s.next == root
        # 
        # Even Case
        #
        # 1 2 3 4 None
        # s   f
        #   s     f
        # s.next == root
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow.next is root
        tmp_root = slow.next
        # Cut the current list in half
        slow.next = None
        # Recursion
        root = TreeNode(tmp_root.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp_root.next)
        return root
        