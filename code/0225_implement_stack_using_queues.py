class MyStack:

    def __init__(self):
        self.q1 = deque([])
        self.stack_top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.stack_top = x

    def pop(self) -> int:
        for i in range(len(self.q1) - 2):
            self.q1.append(self.q1.popleft())
        # Leave two elements, update top element with the first and 
        # return and pop the second
        self.stack_top = self.q1.popleft()
        self.q1.append(self.stack_top)
        return self.q1.popleft()

    def top(self) -> int:
        return self.stack_top

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()