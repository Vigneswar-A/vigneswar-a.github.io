class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lo,hi = intervals[0]
        res = []
        for i,j in intervals:
            if i <= hi:
                hi = max(hi, j)
            else:
                res.append((lo, hi))
                lo, hi = i, j
        res.append((lo, hi))
        return res
                
                
        