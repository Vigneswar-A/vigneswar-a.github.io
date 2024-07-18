class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        start_time = -inf
        res = 0
        
        for time in timeSeries:
            res += min(duration, time-start_time)
            start_time = time
                
        return res
            
                
        