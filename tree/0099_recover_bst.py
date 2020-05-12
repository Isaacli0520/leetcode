# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Morris Inorder Traversal O(1) Space
    def recoverTree(self, root: TreeNode) -> None:                                   
        root, prev, drops = root, TreeNode(float('-inf')), []            
        while root:                                                    
            if root.left:          
                # go to the right most node of root's left subtree
                temp = root.left                                                
                while temp.right and temp.right != root: 
                    temp = temp.right
                # if thread doesn't exist, connect to root
                if not temp.right:                                           
                    temp.right = root
                    root = root.left                     
                    continue    
                # if thread exists, disconnect it
                temp.right = None                                              
            if root.val < prev.val:
                drops.append((prev, root))
            prev = root
            root = root.right                                        
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val      
    
    # Inorder Traversal O(n) Space
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = None
        self.helper(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def helper(self, root):
        if root:
            self.helper(root.left)
            
            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev 
                self.second = root
            self.prev = root
            
            self.helper(root.right)

    