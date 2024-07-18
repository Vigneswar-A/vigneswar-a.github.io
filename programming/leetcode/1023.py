class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        times = self.hashmap[key]
        left = 0
        right = len(times)
        
        while left < right:
            mid = left+right >> 1
            
            if times[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        if right == 0:
            return ""
        
        return times[right-1][1]
        
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)