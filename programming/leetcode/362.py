class HitCounter:

    def __init__(self):
        self.hitmap = defaultdict(lambda : 0)

    def hit(self, timestamp: int) -> None:
        self.hitmap[timestamp] += 1
        
    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(timestamp - 299 , timestamp + 1):
            res += self.hitmap[i]        
        return res
        
        
        
        
    
            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)