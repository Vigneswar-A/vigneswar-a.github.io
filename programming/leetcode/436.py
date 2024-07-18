class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        sorted_intervals = sorted((u,v,i) for i,(u,v) in enumerate(intervals))
        
        
        res = []
        
        for u,v in intervals:
            idx = bisect.bisect_left(sorted_intervals, v, key = lambda tup:tup[0])
            if idx < len(sorted_intervals):
                res.append(sorted_intervals[idx][-1])
            else:
                res.append(-1)
            
        return res
    
