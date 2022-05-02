# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
    
    # Reservoir Sampling
    # Random sampling over a population of unknown size with constant space
    # Probability of selecting the ith element among n elements 
    # = 1/i * i/i+1 * i+1/i+2 ... * n-2/n-1 * n-1/n
    # = 1/n
    def getRandom(self) -> int:
        curr = self.head
        i = 0
        res = curr.val
        while curr:
            r = random.randint(0, i)
            # For element at index i
            #       Probability of selecting it: 1/i
            #   Probability of not selecting it: 1 - 1/i = i - 1 / i
            if r == i:
                res = curr.val
            curr = curr.next
            i += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()