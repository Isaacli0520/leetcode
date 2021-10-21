# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.modes = []
        self.curr_val, self.curr_cnt = 0, 0
        self.max_mode = 0
        def inorder(node, find_max_mode):
            if not node:
                return
            inorder(node.left, find_max_mode)
            # Inorder traversal is like 1 2 3 4 4 4 5 5 6
            # When a new value is encountered, the count
            # starts from 1 again
            if node.val != self.curr_val:
                self.curr_val = node.val
                self.curr_cnt = 0
            self.curr_cnt += 1
            # Record the max mode count
            if self.curr_cnt > self.max_mode:
                self.max_mode = self.curr_cnt
            # Find the mode when max mode count is already found
            elif self.curr_cnt == self.max_mode and not find_max_mode:
                self.modes.append(node.val)
            inorder(node.right, find_max_mode)
            
        # Find Max Mode Count
        inorder(root, True)
        self.curr_val, self.curr_cnt = 0, 0
        # Find Mode
        inorder(root, False)
        return self.modes