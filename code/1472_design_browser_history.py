class BrowserHistory:
    # O(1) time complexity
    # Use a bound variable to store the end of current history
    # so that there is no need to pop every history that comes after
    # current page
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.end = 0

    def visit(self, url: str) -> None:
        if self.curr == len(self.history) - 1:
            self.history.append(url)
        else:
            self.history[self.curr + 1] = url
        self.curr += 1
        self.end = self.curr
            

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += min(steps, self.end - self.curr)
        return self.history[self.curr]

    # Using two stacks
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.fwd = []

    def visit(self, url: str) -> None:
        self.fwd = []
        self.history.append(url)

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.history) - 1)
        for i in range(steps):
            self.fwd.append(self.history.pop())
        return self.history[-1]

    def forward(self, steps: int) -> str:
        steps =  min(len(self.fwd), steps)
        for i in range(steps):
            self.history.append(self.fwd.pop())
        return self.history[-1]

# Doubly-Linked List
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.prev:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.next:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val

class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)