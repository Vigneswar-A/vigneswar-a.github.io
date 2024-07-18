class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda a:(a[1], a[0]))
        
        n = len(intervals)
        
        e = -inf
        count = 0
        for i in range(n):
            if intervals[i][0] >= e:
                count += 1
                e = intervals[i][1]
        
        return n-count
                
          
         
        
                
        
                       
                       
        