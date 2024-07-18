class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        
        if len(bloomDay)//k < m:
            return -1
        
        def is_possible(passed_days):
            cont = 0
            bouquets = 0
            
            for day in bloomDay:
                if day - passed_days <= 0:
                    cont += 1
                else:
                    cont = 0
                    
                if cont == k:
                    bouquets += 1
                    cont = 0
                    
            return bouquets >= m
        
        return bisect.bisect_left(range(10**9), key=is_possible, x=1)
                    
                
        