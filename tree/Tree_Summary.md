# Tree Summary
### Preorder, Inorder, Postorder Traversal Iteratively
** Preorder **
```
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
** Inorder **
```
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

** Postorder **
```
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