class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        
        last_rain = {}
        dry_days = []
        res = [-1] * len(rains)
        
        for day,rain in enumerate(rains):
            if rain == 0:
                dry_days.append(day)
                res[day] = 1
                continue
                
            if rain in last_rain:
                left = 0
                right = len(dry_days)
                while left <= right:
                    mid = left+right >> 1
                    if mid >= len(dry_days):
                        return []
                    if dry_days[mid] < last_rain[rain]:
                        left = mid+1
                    else:
                        right = mid-1
                dry_day = dry_days[left]
                if dry_day < last_rain[rain]:
                    return []
                else:
                    res[dry_day] = rain
                dry_days.remove(dry_day)
            
            last_rain[rain] = day
            
        return res
            
        
                
        
                
                
                
            
            