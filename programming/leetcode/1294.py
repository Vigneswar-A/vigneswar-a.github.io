class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.occurances = defaultdict(list)
        for i,n in enumerate(arr):
            self.occurances[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        l,r = left,right
        isvalid = lambda num: l <= num <= r
        left,right = 0,len(self.occurances[value])
        
        while left<right:
            mid = left+right >> 1
            
            if self.occurances[value][mid] >= l:
                right = mid
            else:
                left = mid+1
        i = left
        left,right = 0,len(self.occurances[value])
        while left<right:
            mid = left+right >> 1
            
            if self.occurances[value][mid] <= r:
                left = mid+1
            else:
                right = mid

        return right - i  
                


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)