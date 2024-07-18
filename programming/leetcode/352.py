class SummaryRanges:

    def __init__(self):
        self.nums = [0]*(10**4 + 2)
        

    def addNum(self, value: int) -> None:
        self.nums[value] = 1
        

    def getIntervals(self) -> List[List[int]]:
        ranges = []
        start = None
        for i in range(10**4+2):
            if self.nums[i]:
                if start is None:
                    start = i
            elif start is not None:
                ranges.append((start, i-1))
                start = None
       

        return ranges
                
                
            
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()