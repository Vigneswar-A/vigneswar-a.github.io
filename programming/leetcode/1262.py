class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.occurances = defaultdict(list)
        for i,num in enumerate(arr):
            self.occurances[num].append(i)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        
        for i in range(10):
            res = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.occurances[res], left)
            r = bisect.bisect(self.occurances[res], right)
            if r-l >= threshold:
                return res
        return -1
            

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)