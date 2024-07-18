class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.stack2 = []
        

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.stack2.clear()
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.stack) > 1:
                self.stack2.append(self.stack.pop())
        return self.stack[-1]
        
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.stack2):
                self.stack.append(self.stack2.pop())
        return self.stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)