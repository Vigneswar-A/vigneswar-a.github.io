class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
    
        
        to_remove = set()
        
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j or j in to_remove:
                    continue
                x, y = intervals[i]
                u, v = intervals[j]
                
                if x <= u and y >= v:
                    to_remove.add(j)
                    
        return len(intervals) - len(to_remove)
                    
                
                    
                
        