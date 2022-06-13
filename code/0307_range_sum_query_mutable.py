class NumArray:

    def __init__(self, nums: List[int]):
        
        def helper(start, end):
            if start == end:
                return Node(nums[start], start, end)
            mid = (start + end) // 2
            left = helper(start, mid)
            right = helper(mid + 1, end)
            return Node(left.val + right.val, start, end, left, right)
        self.root = helper(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        
        def helper(node):
            if node.start == node.end and node.start == index:
                node.val = val
                return
            mid = (node.start + node.end) // 2
            if index > mid:
                helper(node.right)
            else:
                helper(node.left)
            node.val = node.left.val + node.right.val
        
        helper(self.root)
                

    def sumRange(self, left: int, right: int) -> int:
        def helper(node, start, end):
            if node.start == start and node.end == end:
                return node.val
            mid = (node.start + node.end) // 2
            if end <= mid:
                return helper(node.left, start, end)
            elif start > mid:
                return helper(node.right, start, end)
            else:
                return helper(node.left, start, mid) + helper(node.right, mid + 1, end)
        return helper(self.root, left, right)
    
class Node:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.start = start
        self.end = end


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)