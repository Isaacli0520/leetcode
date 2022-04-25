class MyQueue:

    # one stack to take input
    # one stack to show the front of queue
    #
    # For peek, if stack 2 is empty, push all elements into stack 1,
    # and the order of elements will be reversed and thus s2[-1] will
    # be the front of the queue
    # 
    # The above operation is only done when s2 is empty, and thus
    # every element is pushed to s2 once.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()