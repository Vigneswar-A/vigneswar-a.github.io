class MovingAverage:

    def __init__(self, size: int):
        self.container=[]
        self.size=size
        
    def next(self, val: int) -> float:
        self.container.append(val)
        if (size:=len(self.container))>self.size:self.container.pop(0);size-=1
        return sum(self.container)/size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)