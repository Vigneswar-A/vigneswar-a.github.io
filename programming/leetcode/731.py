from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.nums = SortedDict()
        

    def book(self, start: int, end: int) -> bool:
        if start not in self.nums:
            self.nums[start] = 0
        if end not in self.nums:
            self.nums[end] = 0
        self.nums[start] += 1
        self.nums[end] -= 1
        temp = 0
        for i in self.nums.values():
            temp += i
            if temp > 2:
                
                self.nums[start] -= 1
                self.nums[end] += 1
                return False
                
                
        return True
                
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)