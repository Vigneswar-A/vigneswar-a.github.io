class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        scanline = [0] * (10000002)
        for l,r in intervals:
            scanline[l] += 1
            scanline[r+1] -= 1
          
        return max(accumulate(scanline))
        
        
        