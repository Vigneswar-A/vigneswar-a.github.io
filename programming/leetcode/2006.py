class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [*accumulate(chalk)]
        k %= prefix[-1]
        
        right = len(prefix) - 1
        left = 0 
            
        while left < right:
            mid = left + right >> 1
                
            if prefix[mid] == k:
                return mid + 1
                
            elif prefix[mid] < k:
                left = mid + 1
                    
            else:
                right = mid
                 
        return left
         
         
        
        
        
                
            
        
        
            
        
            
            
            
            
            
            
            
            
            
            
            