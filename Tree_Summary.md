# Tree Summary
## Preorder, Inorder, Postorder Traversal Iteratively
### **Preorder**
```python
def Preorder(root):
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res
```
 ### **Inorder** 

- [94. Binary Tree Inorder Traversal](code/0094_binary_tree_inorder_traversal.py)
- [98. Validate Binary Search Tree](code/0098_validate_binary_search_tree.py)
- [230. Kth Smallest Element in a BST](code/0230_kth_smallest_element_in_a_bst.py)

```python
def Inorder(root):
    stack, res = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res
```

### **Postorder**
```python
def Postorder(root):
    stack = [root]
    res = collections.deque()
    while stack:
        node = stack.pop()
        if node:
            res.appendleft(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res
```