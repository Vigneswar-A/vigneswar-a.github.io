class SmallestInfiniteSet:

    def __init__(self):
    
        self.heap = [*range(1, 1001)]
        self.nums = set(self.heap)
        heapify(self.heap)
        

    def popSmallest(self) -> int:
        smallest = heappop(self.heap)
        self.nums.discard(smallest)
        return smallest
        
        

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.add(num)
            heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)