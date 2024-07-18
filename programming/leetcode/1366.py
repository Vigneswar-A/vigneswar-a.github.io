class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.hashmap = {}
        for i in self.queue:
            if i not in self.hashmap:
                self.hashmap[i] = True
            else:
                self.hashmap[i] = False
        

    def showFirstUnique(self) -> int:
        while self.queue and not self.hashmap[self.queue[0]]:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1
            
        

    def add(self, value: int) -> None:
        if value not in self.hashmap:
            self.hashmap[value] = True
            self.queue.append(value)
        else:
            self.hashmap[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)