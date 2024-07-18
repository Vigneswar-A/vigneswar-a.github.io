class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        point=0
        prefix=tuple(itertools.accumulate([0]+calories))
        
        
        for i in range(len(prefix)-k):
            
            if (cal:=prefix[i+k]-prefix[i])<lower:
                point-=1
                
            if cal>upper:
                point+=1
                
        return point
        