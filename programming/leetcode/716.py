class MaxStack:

    def __init__(self):
        self.container=[]

    def push(self, x: int) -> None:
        self.container.append(x)
            
    def pop(self) -> int:
        if len(self.container)>0:
            return self.container.pop(-1)
        else:
            return 

    def top(self) -> int:
        print(self.container)
        return self.container[-1]
        
    def peekMax(self) -> int:
        return max(self.container)
        
    def popMax(self) -> int:
        if len(self.container)>0:
            return self.container.pop(-1-self.container[::-1].index(max(self.container)))
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()