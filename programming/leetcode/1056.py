class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n = len(weights)
        
        def is_possible(max_weight):
            curr_weight = 0
            day = 0
            for weight in weights:
                if weight > max_weight:
                    return False
                curr_weight += weight
                if curr_weight > max_weight:
                    day += 1
                    curr_weight = weight
                    
            return (day < days)
    
        
        return bisect.bisect_left(range(0,1000000), True, key=is_possible)
                    
                
                       
                       