class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        
        is_Travelled = lambda time : sum(time//t for t in times) >= totalTrips
        
        left,right = 0 , max(times) * totalTrips
        
        while left < right:
            mid = left + right >> 1
            if is_Travelled(mid):
                right = mid
            else:
                left = mid + 1

        return right
        
                
        