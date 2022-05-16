class BrowserHistory:
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

    # Using one array and one pointer
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pointer + 1]
        self.stack.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        self.pointer -= min(steps, self.pointer)
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer += min(len(self.stack) - 1 - self.pointer, steps)
        return self.stack[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)