class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())       
        return self.stack2.pop()
        

    def peek(self) -> int:
        return self.stack2[-1] if self.stack2 else self.stack1[0]
        

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()